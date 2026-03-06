from fastapi import APIRouter, Depends, Query, status

from src.application.use_cases.create_company import CreateCompanyUseCase
from src.application.use_cases.delete_company import DeleteCompanyUseCase
from src.application.use_cases.get_company import GetCompanyUseCase
from src.application.use_cases.list_companies import ListCompaniesUseCase
from src.application.use_cases.update_company import UpdateCompanyUseCase
from src.presentation.dependencies import (
    get_create_company_use_case,
    get_delete_company_use_case,
    get_get_company_use_case,
    get_list_companies_use_case,
    get_update_company_use_case,
)
from src.presentation.schemas.company import (
    CompanyResponse,
    CreateCompanyRequest,
    PaginatedCompanyResponse,
    UpdateCompanyRequest,
)

router = APIRouter(prefix="/api/v1/companies", tags=["companies"])


@router.get("/", response_model=PaginatedCompanyResponse)
async def list_companies(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    search: str | None = Query(None),
    sort_by: str = Query("name"),
    sort_order: str = Query("asc", pattern="^(asc|desc)$"),
    use_case: ListCompaniesUseCase = Depends(get_list_companies_use_case),
) -> PaginatedCompanyResponse:
    result = await use_case.execute(
        page=page,
        page_size=page_size,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    return PaginatedCompanyResponse(
        items=[CompanyResponse.from_entity(c) for c in result.items],
        total=result.total,
        page=result.page,
        page_size=result.page_size,
        total_pages=result.total_pages,
    )


@router.get("/{company_id}", response_model=CompanyResponse)
async def get_company(
    company_id: int,
    use_case: GetCompanyUseCase = Depends(get_get_company_use_case),
) -> CompanyResponse:
    company = await use_case.execute(company_id)
    return CompanyResponse.from_entity(company)


@router.post("/", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
async def create_company(
    request: CreateCompanyRequest,
    use_case: CreateCompanyUseCase = Depends(get_create_company_use_case),
) -> CompanyResponse:
    company = await use_case.execute(request.to_entity())
    return CompanyResponse.from_entity(company)


@router.put("/{company_id}", response_model=CompanyResponse)
async def update_company(
    company_id: int,
    request: UpdateCompanyRequest,
    use_case: UpdateCompanyUseCase = Depends(get_update_company_use_case),
) -> CompanyResponse:
    company = await use_case.execute(company_id, request.to_entity())
    return CompanyResponse.from_entity(company)


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(
    company_id: int,
    use_case: DeleteCompanyUseCase = Depends(get_delete_company_use_case),
) -> None:
    await use_case.execute(company_id)
