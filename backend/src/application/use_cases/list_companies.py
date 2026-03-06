from src.domain.entities.company import Company
from src.domain.entities.paginated_result import PaginatedResult
from src.domain.repositories.company_repository import CompanyRepository


class ListCompaniesUseCase:
    def __init__(self, company_repo: CompanyRepository) -> None:
        self._company_repo = company_repo

    async def execute(
        self,
        page: int = 1,
        page_size: int = 10,
        search: str | None = None,
        sort_by: str = "name",
        sort_order: str = "asc",
    ) -> PaginatedResult[Company]:
        return await self._company_repo.find_paginated(
            page=page,
            page_size=page_size,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )
