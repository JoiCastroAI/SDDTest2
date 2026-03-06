from src.domain.entities.company import Company
from src.domain.repositories.company_repository import CompanyRepository


class CreateCompanyUseCase:
    def __init__(self, company_repo: CompanyRepository) -> None:
        self._company_repo = company_repo

    async def execute(self, company: Company) -> Company:
        return await self._company_repo.create(company)
