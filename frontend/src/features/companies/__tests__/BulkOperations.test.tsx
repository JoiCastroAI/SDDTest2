import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import { configureStore } from '@reduxjs/toolkit';
import { companiesApi } from '../companiesApi';
import CompaniesPage from '../../../pages/CompaniesPage';

const createTestStore = () =>
    configureStore({
        reducer: {
            [companiesApi.reducerPath]: companiesApi.reducer,
        },
        middleware: (getDefault) => getDefault().concat(companiesApi.middleware),
    });

describe('Bulk Operations', () => {
    it('should not show Delete Selected button initially', () => {
        render(
            <Provider store={createTestStore()}>
                <MemoryRouter>
                    <CompaniesPage />
                </MemoryRouter>
            </Provider>,
        );

        expect(screen.queryByText(/Delete Selected/)).toBeNull();
    });
});
