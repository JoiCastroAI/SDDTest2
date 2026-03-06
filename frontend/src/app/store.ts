import { configureStore } from '@reduxjs/toolkit';
import { companiesApi } from '../features/companies/companiesApi';

export const store = configureStore({
    reducer: {
        [companiesApi.reducerPath]: companiesApi.reducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(companiesApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
