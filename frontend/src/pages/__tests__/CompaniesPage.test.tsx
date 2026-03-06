import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import { configureStore } from '@reduxjs/toolkit';
import { companiesApi } from '../../features/companies/companiesApi';
import CompaniesPage from '../CompaniesPage';

const createTestStore = () =>
    configureStore({
        reducer: {
            [companiesApi.reducerPath]: companiesApi.reducer,
        },
        middleware: (getDefault) => getDefault().concat(companiesApi.middleware),
    });

const renderPage = () =>
    render(
        <Provider store={createTestStore()}>
            <MemoryRouter>
                <CompaniesPage />
            </MemoryRouter>
        </Provider>,
    );

describe('CompaniesPage', () => {
    it('should render page title', () => {
        renderPage();
        expect(screen.getByText('Companies')).toBeDefined();
    });

    it('should render subtitle', () => {
        renderPage();
        expect(screen.getByText('Manage all companies registered in the system')).toBeDefined();
    });

    it('should render New Company button', () => {
        renderPage();
        expect(screen.getByText('New Company')).toBeDefined();
    });

    it('should render search input', () => {
        renderPage();
        expect(screen.getByPlaceholderText('Search companies...')).toBeDefined();
    });

    it('should show loading spinner initially', () => {
        renderPage();
        expect(screen.getByRole('status')).toBeDefined();
    });
});
