## ADDED Requirements

### Requirement: Companies list page
The system SHALL display a Companies list page at route `/companies` showing a paginated, sortable, searchable table of companies. The table SHALL display columns: name, address (formatted), billing, expenses, profit (computed), employees, clients. The page SHALL support pagination controls, search input, and column sorting.

#### Scenario: List page renders with company data
- **WHEN** the user navigates to /companies
- **THEN** a table SHALL display the first page of companies with all specified columns

#### Scenario: List page displays empty state
- **WHEN** the user navigates to /companies and no companies exist
- **THEN** an empty state message SHALL be displayed

#### Scenario: List page shows loading state
- **WHEN** the companies data is being fetched
- **THEN** a loading indicator SHALL be displayed

#### Scenario: List page shows error state
- **WHEN** the companies data fetch fails
- **THEN** an error message SHALL be displayed

#### Scenario: Pagination controls navigate pages
- **WHEN** the user clicks the next page button
- **THEN** the table SHALL display the next page of results and pagination metadata SHALL update

#### Scenario: Search filters the company list
- **WHEN** the user types a search term in the search input
- **THEN** the table SHALL display only companies matching the search term

#### Scenario: Column sorting orders results
- **WHEN** the user clicks a sortable column header
- **THEN** the table SHALL re-sort results by that column and toggle sort direction on repeated clicks

### Requirement: Create company modal
The system SHALL provide a "New Company" button that opens a modal dialog with a sectioned form containing: Basic Info (name), Address (street, city, state, zip_code, country), Financial Data (billing, expenses, profit display), and Other Data (employees, clients). Profit SHALL be auto-calculated in real-time as billing and expenses values change. Submitting the form SHALL call the create API endpoint.

#### Scenario: Create modal opens on button click
- **WHEN** the user clicks the "New Company" button
- **THEN** a modal dialog SHALL appear with the sectioned company form

#### Scenario: Profit auto-calculates in create form
- **WHEN** the user enters billing=50000 and expenses=30000 in the create form
- **THEN** the profit display SHALL show 20000

#### Scenario: Successful company creation
- **WHEN** the user fills all required fields and submits the create form
- **THEN** the company SHALL be created via the API and the list SHALL refresh

#### Scenario: Create form validation
- **WHEN** the user submits the create form with missing required fields
- **THEN** validation errors SHALL be displayed on the form

### Requirement: Edit company modal
The system SHALL provide an edit action per company row that opens a modal dialog pre-populated with the company's current data. The form layout SHALL match the create modal. Submitting SHALL call the update API endpoint.

#### Scenario: Edit modal opens with pre-populated data
- **WHEN** the user clicks the edit action for a company
- **THEN** a modal dialog SHALL appear with the company's current data pre-filled

#### Scenario: Successful company update
- **WHEN** the user modifies fields and submits the edit form
- **THEN** the company SHALL be updated via the API and the list SHALL refresh

### Requirement: Bulk selection and delete
The system SHALL provide checkbox selection on each table row and a header checkbox for select-all. When one or more rows are selected, a "Delete Selected" action button SHALL appear. Clicking it SHALL prompt for confirmation and then delete each selected company via the API.

#### Scenario: Select individual rows
- **WHEN** the user checks a row's checkbox
- **THEN** the row SHALL be visually marked as selected and the "Delete Selected" button SHALL appear

#### Scenario: Select all rows
- **WHEN** the user checks the header checkbox
- **THEN** all visible rows SHALL be selected

#### Scenario: Bulk delete with confirmation
- **WHEN** the user clicks "Delete Selected" with 3 rows selected
- **THEN** a confirmation dialog SHALL appear, and upon confirmation, all 3 companies SHALL be deleted and the list SHALL refresh

### Requirement: Collapsible sidebar navigation
The system SHALL provide a shared sidebar navigation component with collapsible behavior. The sidebar SHALL contain navigation links including at minimum Dashboard and Companies. The sidebar state (expanded/collapsed) SHALL persist across page navigations.

#### Scenario: Sidebar renders with navigation links
- **WHEN** the application loads
- **THEN** the sidebar SHALL display navigation links for Dashboard and Companies

#### Scenario: Sidebar collapses and expands
- **WHEN** the user clicks the sidebar toggle
- **THEN** the sidebar SHALL collapse (or expand) and the main content area SHALL adjust accordingly

#### Scenario: Active route is highlighted
- **WHEN** the user is on the /companies route
- **THEN** the Companies link in the sidebar SHALL be visually highlighted as active

### Requirement: RTK Query companies API slice
The system SHALL define an RTK Query API slice (`companiesApi`) with endpoints for list (with pagination/search/sort params), get by id, create, update, and delete. Mutations SHALL invalidate the list cache tag to trigger automatic refetch.

#### Scenario: List endpoint fetches paginated companies
- **WHEN** the list endpoint is called with page=1 and page_size=10
- **THEN** the hook SHALL return data with items array and pagination metadata

#### Scenario: Create mutation invalidates list cache
- **WHEN** a company is created via the create endpoint
- **THEN** the list cache tag SHALL be invalidated causing the list to refetch

#### Scenario: Delete mutation invalidates list cache
- **WHEN** a company is deleted via the delete endpoint
- **THEN** the list cache tag SHALL be invalidated causing the list to refetch

**Design References:** UI implementation must follow Figma designs. Referenced nodes: 1:3 (Sidebar), 1:549 (Companies list), 1:1230 (Create modal), 1:1675 (Edit modal).
