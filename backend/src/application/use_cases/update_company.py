from src.domain.entities.company import Company
from src.domain.exceptions import NotFoundError
from src.domain.repositories.company_repository import CompanyRepository


class UpdateCompanyUseCase:
    def __init__(self, company_repo: CompanyRepository) -> None:
        self._company_repo = company_repo

    async def execute(self, company_id: int, company: Company) -> Company:
        existing = await self._company_repo.get_by_id(company_id)
        if existing is None:
            raise NotFoundError("Company", company_id)
        company.id = company_id
        return await self._company_repo.update(company)
