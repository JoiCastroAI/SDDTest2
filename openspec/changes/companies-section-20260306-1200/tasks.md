## 1. [BE] Domain Layer

- [ ] 1.1 [BE] Create Company domain entity dataclass with computed profit property
- [ ] 1.2 [BE] Create PaginatedResult generic dataclass
- [ ] 1.3 [BE] Create CompanyRepository abstract interface (create, get_by_id, update, delete, find_paginated)

## 2. [BE] Persistence Layer

- [ ] 2.1 [BE] Create Alembic migration for companies table
- [ ] 2.2 [BE] Create SQLAlchemy Company model
- [ ] 2.3 [BE] Implement SQLAlchemyCompanyRepository with CRUD and paginated query (search, sort)

## 3. [BE] Application Layer

- [ ] 3.1 [BE] Implement CreateCompanyUseCase
- [ ] 3.2 [BE] Implement GetCompanyUseCase (with NOT_FOUND error)
- [ ] 3.3 [BE] Implement ListCompaniesUseCase (delegates pagination to repository)
- [ ] 3.4 [BE] Implement UpdateCompanyUseCase (with NOT_FOUND error)
- [ ] 3.5 [BE] Implement DeleteCompanyUseCase (with NOT_FOUND error)

## 4. [BE] API Layer

- [ ] 4.1 [BE] Create Pydantic schemas (CreateCompanyRequest, UpdateCompanyRequest, CompanyResponse with computed profit)
- [ ] 4.2 [BE] Create companies router with 5 REST endpoints (GET list, GET by id, POST, PUT, DELETE)
- [ ] 4.3 [BE] Register companies router in the application

## 5. [BE] Documentation

- [ ] 5.1 [BE] Update api-spec.yml with Companies endpoints
- [ ] 5.2 [BE] Update data-model.md with companies table schema

## 6. [FE] Design Sync and Data Layer

- [ ] 6.1 [FE] Sync layout/components from Figma nodes (1:3, 1:549, 1:1230, 1:1675) — extract structure, spacing, and component hierarchy via Live Design Mode
- [ ] 6.2 [FE] Define Company TypeScript types and interfaces
- [ ] 6.3 [FE] Create RTK Query companiesApi slice (list, get, create, update, delete endpoints with tag invalidation)

## 7. [FE] Shared Layout

- [ ] 7.1 [FE] Implement collapsible Sidebar navigation component (Dashboard + Companies links, active route highlight) — must match Figma node 1:3
- [ ] 7.2 [FE] Integrate Sidebar into application layout wrapping route content

## 8. [FE] Companies List Page

- [ ] 8.1 [FE] Implement CompaniesPage with paginated table (columns: name, address, billing, expenses, profit, employees, clients) — must match Figma node 1:549
- [ ] 8.2 [FE] Add search input with debounced filtering
- [ ] 8.3 [FE] Add column sorting (click header to toggle asc/desc)
- [ ] 8.4 [FE] Add pagination controls
- [ ] 8.5 [FE] Add empty, loading, and error states

## 9. [FE] Company Modals

- [ ] 9.1 [FE] Implement CompanyForm component with sectioned layout (Basic Info, Address, Financial Data, Other Data) and real-time profit calculation
- [ ] 9.2 [FE] Implement Create Company modal with "New Company" button trigger — must match Figma node 1:1230
- [ ] 9.3 [FE] Implement Edit Company modal with row action trigger and pre-populated data — must match Figma node 1:1675
- [ ] 9.4 [FE] Add form validation for required fields

## 10. [FE] Bulk Operations

- [ ] 10.1 [FE] Add checkbox selection column with select-all header checkbox
- [ ] 10.2 [FE] Implement "Delete Selected" button with confirmation dialog
- [ ] 10.3 [FE] Wire bulk delete to sequential API calls with list refresh

## 11. [FE] Routing

- [ ] 11.1 [FE] Add /companies route to application router

## 12. [TEST] Backend Tests

- [ ] 12.1 [TEST] Unit tests for Company entity (computed profit, field validation)
- [ ] 12.2 [TEST] Unit tests for all five use cases (happy path + NOT_FOUND errors)
- [ ] 12.3 [TEST] Integration tests for SQLAlchemyCompanyRepository (CRUD, pagination, search, sort)
- [ ] 12.4 [TEST] Integration tests for companies API endpoints (all 5 endpoints, status codes, error responses)

## 13. [TEST] Frontend Tests

- [ ] 13.1 [TEST] Unit tests for companiesApi RTK Query slice (endpoints, cache invalidation)
- [ ] 13.2 [TEST] Component tests for CompanyForm (sections, profit calculation, validation)
- [ ] 13.3 [TEST] Component tests for CompaniesPage (table rendering, search, sort, pagination, states)
- [ ] 13.4 [TEST] Component tests for Sidebar (navigation links, collapse/expand, active route)
- [ ] 13.5 [TEST] Component tests for bulk selection and delete flow

## 14. [E2E] End-to-End Tests

- [ ] 14.1 [E2E] Cypress: Navigate to /companies, verify list loads with pagination
- [ ] 14.2 [E2E] Cypress: Create a new company via modal, verify it appears in list
- [ ] 14.3 [E2E] Cypress: Edit an existing company, verify changes persist
- [ ] 14.4 [E2E] Cypress: Select multiple companies and bulk delete, verify removal
- [ ] 14.5 [E2E] Cypress: Sidebar navigation between Dashboard and Companies

> **Note:** Missing full Figma file URL (FILEKEY). `/opsx:apply` will request Figma node-id URLs for Live Design Mode during frontend implementation.
