## ADDED Requirements

### Requirement: Company domain entity
The system SHALL define a `Company` domain entity as a Python dataclass with fields: `id`, `name`, `street`, `city`, `state`, `zip_code`, `country`, `billing`, `expenses`, `employees`, `clients`, `created_at`, `updated_at`. The entity SHALL expose a computed `profit` property calculated as `billing - expenses`.

#### Scenario: Entity exposes computed profit
- **WHEN** a Company entity has billing=50000 and expenses=30000
- **THEN** the profit property SHALL return 20000

#### Scenario: Entity created with all required fields
- **WHEN** a Company entity is instantiated with name, street, city, state, zip_code, country, billing, expenses, employees, clients
- **THEN** the entity SHALL be valid and all fields SHALL be accessible

### Requirement: Company repository interface
The system SHALL define a `CompanyRepository` abstract interface with methods: `create`, `get_by_id`, `update`, `delete`, and `find_paginated`. The `find_paginated` method SHALL accept `page`, `page_size`, `search`, `sort_by`, and `sort_order` parameters and return a `PaginatedResult[Company]` containing `items`, `total`, `page`, `page_size`, and `total_pages`.

#### Scenario: Repository find_paginated returns paginated results
- **WHEN** the repository contains 25 companies and find_paginated is called with page=2 and page_size=10
- **THEN** the result SHALL contain 10 items, total=25, page=2, page_size=10, total_pages=3

#### Scenario: Repository find_paginated with search filter
- **WHEN** find_paginated is called with search="acme"
- **THEN** the result SHALL contain only companies whose name matches the search term

#### Scenario: Repository find_paginated with sorting
- **WHEN** find_paginated is called with sort_by="name" and sort_order="asc"
- **THEN** the result items SHALL be sorted by name in ascending order

### Requirement: SQLAlchemy repository implementation
The system SHALL implement `CompanyRepository` using SQLAlchemy with a `companies` database table. The implementation SHALL map between the SQLAlchemy model and the domain entity. Search SHALL perform case-insensitive partial matching on the `name` field.

#### Scenario: Create persists company to database
- **WHEN** a valid Company entity is passed to the create method
- **THEN** the company SHALL be persisted in the database and the returned entity SHALL have an assigned id

#### Scenario: Get by non-existent id returns None
- **WHEN** get_by_id is called with an id that does not exist
- **THEN** the method SHALL return None

#### Scenario: Delete removes company from database
- **WHEN** delete is called with a valid company id
- **THEN** the company SHALL no longer exist in the database

### Requirement: Alembic migration for companies table
The system SHALL provide an Alembic migration that creates the `companies` table with columns: id (INTEGER PK autoincrement), name (VARCHAR 255 NOT NULL), street (VARCHAR 255 NOT NULL), city (VARCHAR 100 NOT NULL), state (VARCHAR 100 NOT NULL), zip_code (VARCHAR 20 NOT NULL), country (VARCHAR 100 NOT NULL), billing (NUMERIC 12,2 NOT NULL default 0), expenses (NUMERIC 12,2 NOT NULL default 0), employees (INTEGER NOT NULL default 0), clients (INTEGER NOT NULL default 0), created_at (TIMESTAMP NOT NULL default now), updated_at (TIMESTAMP NOT NULL default now).

#### Scenario: Migration creates companies table
- **WHEN** the migration is applied to an empty database
- **THEN** the `companies` table SHALL exist with all specified columns and constraints

#### Scenario: Migration rollback drops companies table
- **WHEN** the migration is rolled back
- **THEN** the `companies` table SHALL no longer exist

### Requirement: Company use cases
The system SHALL implement five use cases following Clean Architecture: `CreateCompanyUseCase`, `GetCompanyUseCase`, `ListCompaniesUseCase`, `UpdateCompanyUseCase`, `DeleteCompanyUseCase`. Each use case SHALL depend on the `CompanyRepository` interface via dependency injection.

#### Scenario: CreateCompanyUseCase creates a company
- **WHEN** CreateCompanyUseCase is executed with valid company data
- **THEN** a new Company entity SHALL be persisted and returned

#### Scenario: GetCompanyUseCase with valid id
- **WHEN** GetCompanyUseCase is executed with an existing company id
- **THEN** the corresponding Company entity SHALL be returned

#### Scenario: GetCompanyUseCase with invalid id raises error
- **WHEN** GetCompanyUseCase is executed with a non-existent id
- **THEN** a NOT_FOUND error SHALL be raised

#### Scenario: ListCompaniesUseCase returns paginated results
- **WHEN** ListCompaniesUseCase is executed with pagination parameters
- **THEN** a PaginatedResult SHALL be returned with correct pagination metadata

#### Scenario: UpdateCompanyUseCase updates existing company
- **WHEN** UpdateCompanyUseCase is executed with a valid id and updated data
- **THEN** the company SHALL be updated and the updated entity SHALL be returned

#### Scenario: UpdateCompanyUseCase with invalid id raises error
- **WHEN** UpdateCompanyUseCase is executed with a non-existent id
- **THEN** a NOT_FOUND error SHALL be raised

#### Scenario: DeleteCompanyUseCase deletes existing company
- **WHEN** DeleteCompanyUseCase is executed with an existing company id
- **THEN** the company SHALL be removed from persistence

#### Scenario: DeleteCompanyUseCase with invalid id raises error
- **WHEN** DeleteCompanyUseCase is executed with a non-existent id
- **THEN** a NOT_FOUND error SHALL be raised

### Requirement: Pydantic request/response schemas
The system SHALL define Pydantic schemas: `CreateCompanyRequest` (name, street, city, state, zip_code, country, billing, expenses, employees, clients), `UpdateCompanyRequest` (same fields), and `CompanyResponse` (all fields plus id, profit, created_at, updated_at). The `CompanyResponse` SHALL include profit as a computed field.

#### Scenario: CreateCompanyRequest validates required fields
- **WHEN** a CreateCompanyRequest is constructed without a name
- **THEN** a validation error SHALL be raised

#### Scenario: CompanyResponse includes computed profit
- **WHEN** a CompanyResponse is built from a Company entity with billing=50000 and expenses=30000
- **THEN** the profit field SHALL be 20000

### Requirement: REST API endpoints for Companies
The system SHALL expose five REST endpoints under `/api/v1/companies`: GET (list with pagination/search/sort), GET /{id}, POST, PUT /{id}, DELETE /{id}. List SHALL return a paginated response. Create SHALL return 201. Delete SHALL return 204. Not-found cases SHALL return 404 with error body `{"error": {"message": "...", "code": "NOT_FOUND"}}`. Validation failures SHALL return 422.

#### Scenario: GET /api/v1/companies returns paginated list
- **WHEN** GET /api/v1/companies?page=1&page_size=10 is called
- **THEN** the response status SHALL be 200 with items array and pagination metadata

#### Scenario: GET /api/v1/companies with search
- **WHEN** GET /api/v1/companies?search=acme is called
- **THEN** the response SHALL contain only companies matching "acme"

#### Scenario: GET /api/v1/companies/{id} returns company
- **WHEN** GET /api/v1/companies/1 is called for an existing company
- **THEN** the response status SHALL be 200 with the CompanyResponse body

#### Scenario: GET /api/v1/companies/{id} not found
- **WHEN** GET /api/v1/companies/999 is called for a non-existent company
- **THEN** the response status SHALL be 404 with NOT_FOUND error body

#### Scenario: POST /api/v1/companies creates company
- **WHEN** POST /api/v1/companies is called with valid CreateCompanyRequest body
- **THEN** the response status SHALL be 201 with the created CompanyResponse

#### Scenario: POST /api/v1/companies validation error
- **WHEN** POST /api/v1/companies is called with missing required fields
- **THEN** the response status SHALL be 422

#### Scenario: PUT /api/v1/companies/{id} updates company
- **WHEN** PUT /api/v1/companies/1 is called with valid UpdateCompanyRequest body
- **THEN** the response status SHALL be 200 with the updated CompanyResponse

#### Scenario: DELETE /api/v1/companies/{id} deletes company
- **WHEN** DELETE /api/v1/companies/1 is called for an existing company
- **THEN** the response status SHALL be 204 with no body
