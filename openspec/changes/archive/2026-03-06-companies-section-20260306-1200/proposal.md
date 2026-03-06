## Why

The application lacks a Companies entity entirely — no data model, no API, and no UI. Company management is a core business capability required to operate the system. This change introduces the full-stack Companies feature: a backend CRUD API following Clean Architecture and a frontend view driven by Figma designs.

## What Changes

- New `Company` domain entity with fields: name, address (street, city, state, zip_code, country), billing, expenses, profit (computed), employees, clients
- New REST API endpoints for Companies CRUD (list with pagination/search/sort, get, create, update, delete)
- New database table (`companies`) with Alembic migration
- New frontend Companies list page with paginated, sortable, searchable table
- New create/edit company modals with sectioned forms
- Bulk selection and bulk delete capability
- Collapsible sidebar navigation component (shared layout)
- Empty state, loading, and error state handling
- Updated `api-spec.yml` and `data-model.md` documentation

## Capabilities

### New Capabilities

- `company-api`: Backend CRUD API for the Companies entity — domain entity, repository, use cases, Pydantic schemas, REST endpoints with pagination, search, and sorting
- `company-ui`: Frontend Companies section — list view, create/edit modals, bulk actions, sidebar navigation. UI must follow Figma designs (node-id references: 1:3, 1:549, 1:1230, 1:1675)

### Modified Capabilities

_None — no existing specs to modify._

## Impact

- **Backend**: New domain entity, repository interface + SQLAlchemy implementation, 5 use cases, Pydantic schemas, router with 5 endpoints, Alembic migration
- **Frontend**: New `features/companies/` module (types, RTK Query/slice, pages, components), new shared sidebar layout component, new route `/companies`
- **Database**: New `companies` table (PostgreSQL)
- **APIs**: 5 new REST endpoints under `/api/v1/companies`
- **Documentation**: `api-spec.yml` and `data-model.md` must be updated
- **Tests**: Unit tests (use cases + Redux/RTK), integration tests (repository + API), Cypress E2E tests
