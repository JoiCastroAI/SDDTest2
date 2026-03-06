from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.use_cases.create_company import CreateCompanyUseCase
from src.application.use_cases.delete_company import DeleteCompanyUseCase
from src.application.use_cases.get_company import GetCompanyUseCase
from src.application.use_cases.list_companies import ListCompaniesUseCase
from src.application.use_cases.update_company import UpdateCompanyUseCase
from src.infrastructure.database.repositories.company_repo import SqlAlchemyCompanyRepository
from src.infrastructure.database.session import get_session


def get_company_repo(session: AsyncSession = Depends(get_session)) -> SqlAlchemyCompanyRepository:
    return SqlAlchemyCompanyRepository(session)


def get_create_company_use_case(
    repo: SqlAlchemyCompanyRepository = Depends(get_company_repo),
) -> CreateCompanyUseCase:
    return CreateCompanyUseCase(repo)


def get_get_company_use_case(
    repo: SqlAlchemyCompanyRepository = Depends(get_company_repo),
) -> GetCompanyUseCase:
    return GetCompanyUseCase(repo)


def get_list_companies_use_case(
    repo: SqlAlchemyCompanyRepository = Depends(get_company_repo),
) -> ListCompaniesUseCase:
    return ListCompaniesUseCase(repo)


def get_update_company_use_case(
    repo: SqlAlchemyCompanyRepository = Depends(get_company_repo),
) -> UpdateCompanyUseCase:
    return UpdateCompanyUseCase(repo)


def get_delete_company_use_case(
    repo: SqlAlchemyCompanyRepository = Depends(get_company_repo),
) -> DeleteCompanyUseCase:
    return DeleteCompanyUseCase(repo)
