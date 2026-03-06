from src.domain.exceptions import NotFoundError
from src.domain.repositories.company_repository import CompanyRepository


class DeleteCompanyUseCase:
    def __init__(self, company_repo: CompanyRepository) -> None:
        self._company_repo = company_repo

    async def execute(self, company_id: int) -> None:
        existing = await self._company_repo.get_by_id(company_id)
        if existing is None:
            raise NotFoundError("Company", company_id)
        await self._company_repo.delete(company_id)
