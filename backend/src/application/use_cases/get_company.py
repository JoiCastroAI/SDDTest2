from src.domain.entities.company import Company
from src.domain.exceptions import NotFoundError
from src.domain.repositories.company_repository import CompanyRepository


class GetCompanyUseCase:
    def __init__(self, company_repo: CompanyRepository) -> None:
        self._company_repo = company_repo

    async def execute(self, company_id: int) -> Company:
        company = await self._company_repo.get_by_id(company_id)
        if company is None:
            raise NotFoundError("Company", company_id)
        return company
