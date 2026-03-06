## 1. [BE] Domain Layer

- [x] 1.1 [BE] Create Company domain entity dataclass with computed profit property
- [x] 1.2 [BE] Create PaginatedResult generic dataclass
- [x] 1.3 [BE] Create CompanyRepository abstract interface (create, get_by_id, update, delete, find_paginated)

## 2. [BE] Persistence Layer

- [x] 2.1 [BE] Create Alembic migration for companies table
- [x] 2.2 [BE] Create SQLAlchemy Company model
- [x] 2.3 [BE] Implement SQLAlchemyCompanyRepository with CRUD and paginated query (search, sort)

## 3. [BE] Application Layer

- [x] 3.1 [BE] Implement CreateCompanyUseCase
- [x] 3.2 [BE] Implement GetCompanyUseCase (with NOT_FOUND error)
- [x] 3.3 [BE] Implement ListCompaniesUseCase (delegates pagination to repository)
- [x] 3.4 [BE] Implement UpdateCompanyUseCase (with NOT_FOUND error)
- [x] 3.5 [BE] Implement DeleteCompanyUseCase (with NOT_FOUND error)

## 4. [BE] API Layer

- [x] 4.1 [BE] Create Pydantic schemas (CreateCompanyRequest, UpdateCompanyRequest, CompanyResponse with computed profit)
- [x] 4.2 [BE] Create companies router with 5 REST endpoints (GET list, GET by id, POST, PUT, DELETE)
- [x] 4.3 [BE] Register companies router in the application

## 5. [BE] Documentation

- [x] 5.1 [BE] Update api-spec.yml with Companies endpoints
- [x] 5.2 [BE] Update data-model.md with companies table schema

## 6. [FE] Design Sync and Data Layer

- [x] 6.1 [FE] Sync layout/components from Figma nodes (1:3, 1:549, 1:1230, 1:1675) — extract structure, spacing, and component hierarchy via Live Design Mode
- [x] 6.2 [FE] Define Company TypeScript types and interfaces
- [x] 6.3 [FE] Create RTK Query companiesApi slice (list, get, create, update, delete endpoints with tag invalidation)

## 7. [FE] Shared Layout

- [x] 7.1 [FE] Implement collapsible Sidebar navigation component (Dashboard + Companies links, active route highlight) — must match Figma node 1:3
- [x] 7.2 [FE] Integrate Sidebar into application layout wrapping route content

## 8. [FE] Companies List Page

- [x] 8.1 [FE] Implement CompaniesPage with paginated table (columns: name, address, billing, expenses, profit, employees, clients) — must match Figma node 1:549
- [x] 8.2 [FE] Add search input with debounced filtering
- [x] 8.3 [FE] Add column sorting (click header to toggle asc/desc)
- [x] 8.4 [FE] Add pagination controls
- [x] 8.5 [FE] Add empty, loading, and error states

## 9. [FE] Company Modals

- [x] 9.1 [FE] Implement CompanyForm component with sectioned layout (Basic Info, Address, Financial Data, Other Data) and real-time profit calculation
- [x] 9.2 [FE] Implement Create Company modal with "New Company" button trigger — must match Figma node 1:1230
- [x] 9.3 [FE] Implement Edit Company modal with row action trigger and pre-populated data — must match Figma node 1:1675
- [x] 9.4 [FE] Add form validation for required fields

## 10. [FE] Bulk Operations

- [x] 10.1 [FE] Add checkbox selection column with select-all header checkbox
- [x] 10.2 [FE] Implement "Delete Selected" button with confirmation dialog
- [x] 10.3 [FE] Wire bulk delete to sequential API calls with list refresh

## 11. [FE] Routing

- [x] 11.1 [FE] Add /companies route to application router

## 12. [TEST] Backend Tests

- [x] 12.1 [TEST] Unit tests for Company entity (computed profit, field validation)
- [x] 12.2 [TEST] Unit tests for all five use cases (happy path + NOT_FOUND errors)
- [x] 12.3 [TEST] Integration tests for SQLAlchemyCompanyRepository (CRUD, pagination, search, sort)
- [x] 12.4 [TEST] Integration tests for companies API endpoints (all 5 endpoints, status codes, error responses)

## 13. [TEST] Frontend Tests

- [x] 13.1 [TEST] Unit tests for companiesApi RTK Query slice (endpoints, cache invalidation)
- [x] 13.2 [TEST] Component tests for CompanyForm (sections, profit calculation, validation)
- [x] 13.3 [TEST] Component tests for CompaniesPage (table rendering, search, sort, pagination, states)
- [x] 13.4 [TEST] Component tests for Sidebar (navigation links, collapse/expand, active route)
- [x] 13.5 [TEST] Component tests for bulk selection and delete flow

## 14. [E2E] End-to-End Tests

- [x] 14.1 [E2E] Cypress: Navigate to /companies, verify list loads with pagination
- [x] 14.2 [E2E] Cypress: Create a new company via modal, verify it appears in list
- [x] 14.3 [E2E] Cypress: Edit an existing company, verify changes persist
- [x] 14.4 [E2E] Cypress: Select multiple companies and bulk delete, verify removal
- [x] 14.5 [E2E] Cypress: Sidebar navigation between Dashboard and Companies

> **Note:** Missing full Figma file URL (FILEKEY). `/opsx:apply` will request Figma node-id URLs for Live Design Mode during frontend implementation.
