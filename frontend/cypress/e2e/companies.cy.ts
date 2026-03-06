const API_URL = Cypress.env('API_URL');

describe('Companies', () => {
    beforeEach(() => {
        cy.visit('/companies');
    });

    it('should navigate to /companies and display the list page', () => {
        cy.contains('Companies').should('be.visible');
        cy.contains('Manage all companies registered in the system').should('be.visible');
        cy.get('input[placeholder="Search companies..."]').should('be.visible');
    });

    it('should create a new company via modal', () => {
        cy.contains('New Company').click();
        cy.contains('New Company').should('be.visible');

        cy.get('input[name="name"]').type('Cypress Corp');
        cy.get('input[name="street"]').type('100 Test Blvd');
        cy.get('input[name="city"]').type('TestCity');
        cy.get('input[name="state"]').type('TC');
        cy.get('input[name="zip_code"]').type('12345');
        cy.get('input[name="country"]').type('US');
        cy.get('input[name="billing"]').clear().type('100000');
        cy.get('input[name="expenses"]').clear().type('50000');
        cy.get('input[name="employees"]').clear().type('25');
        cy.get('input[name="clients"]').clear().type('10');

        cy.contains('Create Company').click();
        cy.contains('Cypress Corp').should('be.visible');
    });

    it('should edit an existing company', () => {
        cy.get('[aria-label^="Edit"]').first().click();
        cy.contains('Edit Company').should('be.visible');

        cy.get('input[name="name"]').clear().type('Updated Corp');
        cy.contains('Save Changes').click();
        cy.contains('Updated Corp').should('be.visible');
    });

    it('should select and bulk delete companies', () => {
        cy.get('input[type="checkbox"]').first().check();
        cy.contains('Delete Selected').click();
        cy.contains('Confirm Delete').should('be.visible');
        cy.get('.modal-footer').contains('Delete').click();
    });
});

describe('Sidebar Navigation', () => {
    it('should navigate between Dashboard and Companies', () => {
        cy.visit('/');
        cy.contains('Dashboard').should('be.visible');

        cy.get('nav').contains('Companies').click();
        cy.url().should('include', '/companies');
        cy.contains('Manage all companies registered in the system').should('be.visible');

        cy.get('nav').contains('Dashboard').click();
        cy.url().should('eq', Cypress.config().baseUrl + '/');
    });
});
