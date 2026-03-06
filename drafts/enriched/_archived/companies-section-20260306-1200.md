<!-- BEGIN_ENRICHED_USER_STORY -->
# Enriched User Story

design-linked: true
scope:
  backend: true
  frontend: true
source: Notion
reference: https://www.notion.so/31a04e35e0538073ad71c7cc64e16cb6

## Title
Companies Section

## Problem / Context
The application needs a Companies entity to manage company data. This requires a full-stack implementation: a Backend CRUD API for the Companies entity following Clean Architecture (Python/FastAPI, PostgreSQL, SQLAlchemy), and a Frontend view (React/TypeScript, Redux Toolkit, React Bootstrap) based on the provided Figma designs. Currently, no Companies entity or UI exists in the system.

## Desired Outcome
- A paginated company listing table with bulk selection capabilities
- Search/filter bar to filter companies by name
- Sortable table columns (Name, Billing, Expenses, Profit, Employees, Clients)
- Bulk delete action for multiple selected companies
- Modal-based workflow to create a new company (sectioned form: Basic Info, Address, Financial Data, Other Data)
- Modal-based workflow to edit an existing company (same sectioned form, pre-populated)
- Auto-calculated profit field (billing - expenses) displayed in modals
- Empty state handling when no companies exist
- Collapsible sidebar navigation with app branding and navigation items (Dashboard, Companies)
- Pagination controls with result count (e.g., "Showing X of Y companies")
- Responsive layout matching the Figma designs
- Full backend CRUD API for the Companies entity

## Acceptance Criteria

### Backend
- BE-AC-1: `Company` domain entity created as a dataclass in `backend/src/domain/entities/` with fields: name, street, city, state, zip_code, country, billing (decimal), expenses (decimal), profit (computed: billing - expenses), employees (int), clients (int)
- BE-AC-2: `CompanyRepository` abstract interface defined in `backend/src/domain/repositories/`
- BE-AC-3: `CompanyModel` SQLAlchemy model created in `backend/src/infrastructure/database/models/`
- BE-AC-4: `SqlAlchemyCompanyRepository` implementation in `backend/src/infrastructure/database/repositories/`
- BE-AC-5: Use cases created in `backend/src/application/use_cases/`: `CreateCompany`, `GetCompany`, `ListCompanies`, `UpdateCompany`, `DeleteCompany`
- BE-AC-6: Pydantic request/response schemas in `backend/src/presentation/schemas/`
- BE-AC-7: REST endpoints in `backend/src/presentation/routers/`:
  - `GET /api/v1/companies` — list with pagination (page, page_size query params) and optional search filter (query param `search` filtering by name)
  - `GET /api/v1/companies/{id}` — get by ID
  - `POST /api/v1/companies` — create
  - `PUT /api/v1/companies/{id}` — update
  - `DELETE /api/v1/companies/{id}` — delete
- BE-AC-8: List endpoint supports sorting via `sort_by` and `sort_order` query params (sortable fields: name, billing, expenses, profit, employees, clients)
- BE-AC-9: Alembic migration created for the `companies` table
- BE-AC-10: Unit tests for all use cases (happy path, error, edge cases) with 90%+ coverage
- BE-AC-11: Integration tests for repository and API endpoints
- BE-AC-12: `api-spec.yml` updated with all new endpoints
- BE-AC-13: `data-model.md` updated with Company entity definition

### Frontend
- FE-AC-1: `Company` TypeScript type defined in `frontend/src/features/companies/types.ts` with fields matching the backend entity
- FE-AC-2: Redux slice (`companiesSlice.ts`) or RTK Query API (`companiesApi.ts`) in `frontend/src/features/companies/`
- FE-AC-3: Companies list page with paginated table, matching Figma design (node 1:549)
- FE-AC-4: Search input field above the table that filters companies by name (placeholder: "Search companies...")
- FE-AC-5: Sortable table columns with sort indicator icons (ArrowUpDown) for: Name, Billing, Expenses, Profit, Employees, Clients
- FE-AC-6: Bulk selection with checkbox column and bulk delete action
- FE-AC-7: Create company modal with sectioned form matching Figma (node 1:1230): Basic Info (name), Address (street, city, state, zip, country), Financial Data (billing, expenses, auto-calculated profit), Other Data (employees, clients). Buttons: Cancel, Create Company
- FE-AC-8: Edit company modal with pre-populated sectioned form matching Figma (node 1:1675). Buttons: Cancel, Save Changes
- FE-AC-9: Empty state component when no companies exist
- FE-AC-10: Loading and error states for all async operations
- FE-AC-11: Responsive layout using React Bootstrap grid
- FE-AC-12: Route added for `/companies` in React Router configuration
- FE-AC-13: Collapsible sidebar navigation component (node 1:3) as a shared layout with: app logo/branding ("FastReport"), collapse toggle button, navigation items (Dashboard, Companies) with active state highlighting
- FE-AC-14: Pagination controls below the table showing result count ("Showing X of Y companies") and page navigation
- FE-AC-15: Per-row action buttons: Edit (pencil icon) and Delete (trash icon), matching Figma design
- FE-AC-16: Cypress E2E tests for: list view, search filtering, create, edit, delete, bulk delete, pagination, sorting
- FE-AC-17: Vitest unit tests for Redux slice/RTK Query and utility functions

## Design References

Figma File:
https://www.figma.com/design/GfsFFzSElzlbM9uhiNJ3jx/Sin-título?node-id=0-1

Referenced Nodes:
- https://www.figma.com/design/GfsFFzSElzlbM9uhiNJ3jx/Sin-título?node-id=1-3
- https://www.figma.com/design/GfsFFzSElzlbM9uhiNJ3jx/Sin-título?node-id=1-549
- https://www.figma.com/design/GfsFFzSElzlbM9uhiNJ3jx/Sin-título?node-id=1-1230
- https://www.figma.com/design/GfsFFzSElzlbM9uhiNJ3jx/Sin-título?node-id=1-1675

### Node Mapping
- **1:3** — Sidebar navigation (collapsible, app branding, Dashboard + Companies nav items)
- **1:549** — Main companies list view (header, search bar, data table with sorting, pagination footer, "New Company" button)
- **1:1230** — Create company modal (sectioned form: Basic Info, Address, Financial Data with auto-calculated profit, Other Data)
- **1:1675** — Edit company modal (same form pre-populated with existing company data, "Save Changes" button)

## Technical Notes
- Backend: Python 3.11+ / FastAPI / SQLAlchemy 2.0+ / PostgreSQL / Alembic / Pytest
- Frontend: React 18+ / TypeScript 5+ / Redux Toolkit / React Bootstrap / Vite / Cypress
- Follow Clean Architecture boundaries (domain → application → infrastructure → presentation)
- All code, comments, and documentation in English
- Pagination response should include: items, total, page, page_size, total_pages
- Profit is a computed field (billing - expenses), calculated server-side and displayed client-side in real-time in modals
- Table columns from Figma: Checkbox, Name, Address, Billing, Expenses, Profit, Employees, Clients, Actions

## Out of Scope
- Authentication/authorization for company endpoints (unless already implemented globally)
- Company logo/image upload

<!-- END_ENRICHED_USER_STORY -->
