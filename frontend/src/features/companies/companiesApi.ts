import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import type {
    Company,
    CompanyListParams,
    CreateCompanyRequest,
    PaginatedResponse,
    UpdateCompanyRequest,
} from '../../types/company';

const API_BASE_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

export const companiesApi = createApi({
    reducerPath: 'companiesApi',
    baseQuery: fetchBaseQuery({ baseUrl: `${API_BASE_URL}/api/v1` }),
    tagTypes: ['Company'],
    endpoints: (builder) => ({
        listCompanies: builder.query<PaginatedResponse<Company>, CompanyListParams>({
            query: (params) => ({
                url: '/companies',
                params: {
                    page: params.page ?? 1,
                    page_size: params.page_size ?? 10,
                    search: params.search || undefined,
                    sort_by: params.sort_by ?? 'name',
                    sort_order: params.sort_order ?? 'asc',
                },
            }),
            providesTags: ['Company'],
        }),
        getCompany: builder.query<Company, number>({
            query: (id) => `/companies/${id}`,
            providesTags: (_result, _error, id) => [{ type: 'Company', id }],
        }),
        createCompany: builder.mutation<Company, CreateCompanyRequest>({
            query: (body) => ({
                url: '/companies',
                method: 'POST',
                body,
            }),
            invalidatesTags: ['Company'],
        }),
        updateCompany: builder.mutation<Company, { id: number; data: UpdateCompanyRequest }>({
            query: ({ id, data }) => ({
                url: `/companies/${id}`,
                method: 'PUT',
                body: data,
            }),
            invalidatesTags: ['Company'],
        }),
        deleteCompany: builder.mutation<void, number>({
            query: (id) => ({
                url: `/companies/${id}`,
                method: 'DELETE',
            }),
            invalidatesTags: ['Company'],
        }),
    }),
});

export const {
    useListCompaniesQuery,
    useGetCompanyQuery,
    useCreateCompanyMutation,
    useUpdateCompanyMutation,
    useDeleteCompanyMutation,
} = companiesApi;
