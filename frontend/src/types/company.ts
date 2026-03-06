export type Company = {
    id: number;
    name: string;
    street: string;
    city: string;
    state: string;
    zip_code: string;
    country: string;
    billing: number;
    expenses: number;
    profit: number;
    employees: number;
    clients: number;
    created_at: string;
    updated_at: string;
};

export type CreateCompanyRequest = {
    name: string;
    street: string;
    city: string;
    state: string;
    zip_code: string;
    country: string;
    billing: number;
    expenses: number;
    employees: number;
    clients: number;
};

export type UpdateCompanyRequest = CreateCompanyRequest;

export type PaginatedResponse<T> = {
    items: T[];
    total: number;
    page: number;
    page_size: number;
    total_pages: number;
};

export type CompanyListParams = {
    page?: number;
    page_size?: number;
    search?: string;
    sort_by?: string;
    sort_order?: 'asc' | 'desc';
};
