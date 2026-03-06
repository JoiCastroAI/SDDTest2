import { describe, it, expect } from 'vitest';
import { companiesApi } from '../companiesApi';

describe('companiesApi', () => {
    it('should define the correct reducer path', () => {
        expect(companiesApi.reducerPath).toBe('companiesApi');
    });

    it('should have Company tag type', () => {
        expect(companiesApi.util).toBeDefined();
    });

    it('should export list endpoint', () => {
        expect(companiesApi.endpoints.listCompanies).toBeDefined();
    });

    it('should export create endpoint', () => {
        expect(companiesApi.endpoints.createCompany).toBeDefined();
    });

    it('should export update endpoint', () => {
        expect(companiesApi.endpoints.updateCompany).toBeDefined();
    });

    it('should export delete endpoint', () => {
        expect(companiesApi.endpoints.deleteCompany).toBeDefined();
    });

    it('should export getCompany endpoint', () => {
        expect(companiesApi.endpoints.getCompany).toBeDefined();
    });
});
