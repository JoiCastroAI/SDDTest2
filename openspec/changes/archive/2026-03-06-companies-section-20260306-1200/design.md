## Context

The application currently has no Companies entity — no database table, no API, and no UI. The backend follows Clean Architecture (Python/FastAPI/SQLAlchemy/PostgreSQL) and the frontend uses React/TypeScript/Redux Toolkit/React Bootstrap. An existing `Candidate` entity demonstrates the established patterns across all layers.

## Goals / Non-Goals

**Goals:**
- Implement a full CRUD lifecycle for Companies following existing Clean Architecture patterns
- Provide a paginated, sortable, searchable list API with standard REST conventions
- Build a frontend Companies section with list view, create/edit modals, and bulk operations
- Match the Figma designs for all UI components
- Maintain test coverage at 90%+ (backend) with Cypress E2E and Vitest unit tests (frontend)

**Non-Goals:**
- Authentication/authorization for company endpoints (out of scope unless globally applied)
- Company logo or image upload
- Multi-tenancy or company hierarchy
- Real-time updates (WebSocket)

## Decisions

### D1: Company domain entity as dataclass with computed profit

The `Company` entity uses `@dataclass` with a `profit` property computed as `billing - expenses`. Profit is not stored in the database — it is calculated on read. This avoids data staleness and aligns with how existing entities (e.g., `Candidate`) are modeled.

**Alternative considered:** Store profit as a database column with a trigger. Rejected because it adds migration complexity and risks stale data if billing/expenses are updated outside the trigger.

### D2: Single repository interface with pagination support

`CompanyRepository` defines a `find_paginated` method accepting `page`, `page_size`, `search`, `sort_by`, and `sort_order` parameters, returning a `PaginatedResult[Company]` dataclass with `items`, `total`, `page`, `page_size`, and `total_pages`.

**Alternative considered:** Separate reader/writer interfaces (ISP). Deferred — all five use cases need both read and write access, so a single interface is simpler for now.

### D3: RTK Query for frontend data fetching

Use RTK Query (`companiesApi.ts`) instead of a Redux slice with `createAsyncThunk`. RTK Query provides automatic caching, tag-based invalidation, and reduces boilerplate. The `companiesApi` will define endpoints for list, get, create, update, and delete, with tag invalidation on mutations.

**Alternative considered:** Manual slice with `createAsyncThunk` (as shown in `candidatesSlice` example). RTK Query is preferred per frontend standards as it eliminates manual loading/error state management.

### D4: Sidebar as a shared layout component

The collapsible sidebar navigation is implemented as a shared layout component (`components/Sidebar.tsx`) wrapping route content, not as a feature-specific component. This allows reuse across Dashboard and Companies pages.

**Alternative considered:** Embed sidebar within each page. Rejected — duplicates layout logic and breaks DRY.

### D5: Modal-based create/edit with sectioned form

Create and edit flows use React Bootstrap `Modal` with a sectioned form (Basic Info, Address, Financial Data, Other Data). Both modals share a single `CompanyForm` component, with mode ("create" | "edit") determining button labels and pre-population behavior. Profit is auto-calculated in real-time as the user types billing/expenses values.

### D6: Bulk delete via multi-select checkboxes

The list table includes a checkbox column for row selection. A "Delete Selected" action button appears when one or more rows are selected. Bulk delete calls `DELETE /api/v1/companies/{id}` sequentially per selected company (no batch endpoint needed for MVP).

**Alternative considered:** Batch delete endpoint (`DELETE /api/v1/companies` with body). Simpler to use individual deletes for now; batch can be added later if performance requires it.

## Data Model

### companies table

| Column     | Type           | Constraints                |
|------------|----------------|----------------------------|
| id         | INTEGER        | PK, autoincrement          |
| name       | VARCHAR(255)   | NOT NULL                   |
| street     | VARCHAR(255)   | NOT NULL                   |
| city       | VARCHAR(100)   | NOT NULL                   |
| state      | VARCHAR(100)   | NOT NULL                   |
| zip_code   | VARCHAR(20)    | NOT NULL                   |
| country    | VARCHAR(100)   | NOT NULL                   |
| billing    | NUMERIC(12,2)  | NOT NULL, default 0        |
| expenses   | NUMERIC(12,2)  | NOT NULL, default 0        |
| employees  | INTEGER        | NOT NULL, default 0        |
| clients    | INTEGER        | NOT NULL, default 0        |
| created_at | TIMESTAMP      | NOT NULL, default now()    |
| updated_at | TIMESTAMP      | NOT NULL, default now()    |

`profit` is computed as `billing - expenses` at the application/presentation layer, not stored.

## API Contracts

### List Companies
```
GET /api/v1/companies?page=1&page_size=10&search=acme&sort_by=name&sort_order=asc

Response 200:
{
  "items": [CompanyResponse],
  "total": 42,
  "page": 1,
  "page_size": 10,
  "total_pages": 5
}
```

### Get Company
```
GET /api/v1/companies/{id}

Response 200: CompanyResponse
Response 404: { "error": { "message": "Company not found: {id}", "code": "NOT_FOUND" } }
```

### Create Company
```
POST /api/v1/companies
Body: CreateCompanyRequest (name, street, city, state, zip_code, country, billing, expenses, employees, clients)

Response 201: CompanyResponse
Response 422: Pydantic validation error
```

### Update Company
```
PUT /api/v1/companies/{id}
Body: UpdateCompanyRequest (same fields as create)

Response 200: CompanyResponse
Response 404: NOT_FOUND
```

### Delete Company
```
DELETE /api/v1/companies/{id}

Response 204: No content
Response 404: NOT_FOUND
```

### CompanyResponse schema
```json
{
  "id": 1,
  "name": "Acme Corp",
  "street": "123 Main St",
  "city": "Springfield",
  "state": "IL",
  "zip_code": "62701",
  "country": "US",
  "billing": 50000.00,
  "expenses": 30000.00,
  "profit": 20000.00,
  "employees": 150,
  "clients": 42,
  "created_at": "2026-03-06T12:00:00Z",
  "updated_at": "2026-03-06T12:00:00Z"
}
```

## Live Design Mode

Frontend implementation must consult the Figma MCP at apply time for accurate layout, spacing, colors, and component structure. The referenced Figma nodes are:
- **1:3** — Sidebar navigation
- **1:549** — Companies list view
- **1:1230** — Create company modal
- **1:1675** — Edit company modal

## Risks / Trade-offs

- **[Risk] Sequential bulk delete may be slow for large selections** → Acceptable for MVP; add batch endpoint if needed
- **[Risk] Profit computed on every read** → Negligible cost for CRUD operations; database-level computed column can be added later if reporting queries need it
- **[Trade-off] Single repository interface** → Simpler now but may need ISP split if read-only consumers emerge
- **[Trade-off] No optimistic updates on mutations** → RTK Query tag invalidation refetches the list; optimistic updates can be added for perceived performance later
