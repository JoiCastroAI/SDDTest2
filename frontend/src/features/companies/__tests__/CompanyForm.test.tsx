import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import CompanyForm from '../CompanyForm';

describe('CompanyForm', () => {
    it('should render all four sections', () => {
        render(<CompanyForm formId="test" onSubmit={vi.fn()} />);

        expect(screen.getByText('Basic Info')).toBeDefined();
        expect(screen.getByText('Address')).toBeDefined();
        expect(screen.getByText('Financial Data')).toBeDefined();
        expect(screen.getByText('Other Data')).toBeDefined();
    });

    it('should display calculated profit', () => {
        render(<CompanyForm formId="test" onSubmit={vi.fn()} />);

        const billingInput = screen.getByLabelText(/Billing/i) as HTMLInputElement;
        const expensesInput = screen.getByLabelText(/Expenses/i) as HTMLInputElement;

        fireEvent.change(billingInput, { target: { value: '5000000', name: 'billing' } });
        fireEvent.change(expensesInput, { target: { value: '3000000', name: 'expenses' } });

        expect(screen.getByText('$2.00M')).toBeDefined();
    });

    it('should pre-populate data when initialData is provided', () => {
        const company = {
            id: 1,
            name: 'Test Corp',
            street: '123 Main',
            city: 'Austin',
            state: 'TX',
            zip_code: '73301',
            country: 'US',
            billing: 50000,
            expenses: 30000,
            profit: 20000,
            employees: 10,
            clients: 5,
            created_at: '2026-01-01',
            updated_at: '2026-01-01',
        };

        render(<CompanyForm formId="test" onSubmit={vi.fn()} initialData={company} />);

        const nameInput = screen.getByDisplayValue('Test Corp') as HTMLInputElement;
        expect(nameInput).toBeDefined();
    });

    it('should show validation on invalid submit', () => {
        const onSubmit = vi.fn();
        render(<CompanyForm formId="test-form" onSubmit={onSubmit} />);

        const form = document.getElementById('test-form') as HTMLFormElement;
        fireEvent.submit(form);

        expect(onSubmit).not.toHaveBeenCalled();
    });
});
