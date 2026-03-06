from datetime import datetime
from decimal import Decimal

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.company import Company
from src.domain.entities.paginated_result import PaginatedResult
from src.domain.repositories.company_repository import CompanyRepository
from src.infrastructure.database.models.company import CompanyModel


class SqlAlchemyCompanyRepository(CompanyRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, company: Company) -> Company:
        model = self._to_model(company)
        self._session.add(model)
        await self._session.flush()
        return self._to_entity(model)

    async def get_by_id(self, company_id: int) -> Company | None:
        result = await self._session.get(CompanyModel, company_id)
        return self._to_entity(result) if result else None

    async def update(self, company: Company) -> Company:
        model = await self._session.get(CompanyModel, company.id)
        if model is None:
            raise ValueError(f"Company not found: {company.id}")
        model.name = company.name
        model.street = company.street
        model.city = company.city
        model.state = company.state
        model.zip_code = company.zip_code
        model.country = company.country
        model.billing = float(company.billing)
        model.expenses = float(company.expenses)
        model.employees = company.employees
        model.clients = company.clients
        model.updated_at = datetime.utcnow()
        await self._session.flush()
        return self._to_entity(model)

    async def delete(self, company_id: int) -> None:
        model = await self._session.get(CompanyModel, company_id)
        if model is not None:
            await self._session.delete(model)
            await self._session.flush()

    async def find_paginated(
        self,
        page: int = 1,
        page_size: int = 10,
        search: str | None = None,
        sort_by: str = "name",
        sort_order: str = "asc",
    ) -> PaginatedResult[Company]:
        query = select(CompanyModel)
        count_query = select(func.count()).select_from(CompanyModel)

        if search:
            search_filter = CompanyModel.name.ilike(f"%{search}%")
            query = query.where(search_filter)
            count_query = count_query.where(search_filter)

        total_result = await self._session.execute(count_query)
        total = total_result.scalar() or 0

        sortable_columns = {
            "name": CompanyModel.name,
            "city": CompanyModel.city,
            "state": CompanyModel.state,
            "country": CompanyModel.country,
            "billing": CompanyModel.billing,
            "expenses": CompanyModel.expenses,
            "employees": CompanyModel.employees,
            "clients": CompanyModel.clients,
            "created_at": CompanyModel.created_at,
        }
        sort_column = sortable_columns.get(sort_by, CompanyModel.name)
        if sort_order == "desc":
            sort_column = sort_column.desc()

        offset = (page - 1) * page_size
        query = query.order_by(sort_column).offset(offset).limit(page_size)

        result = await self._session.execute(query)
        models = result.scalars().all()

        return PaginatedResult(
            items=[self._to_entity(m) for m in models],
            total=total,
            page=page,
            page_size=page_size,
        )

    def _to_entity(self, model: CompanyModel) -> Company:
        return Company(
            id=model.id,
            name=model.name,
            street=model.street,
            city=model.city,
            state=model.state,
            zip_code=model.zip_code,
            country=model.country,
            billing=Decimal(str(model.billing)),
            expenses=Decimal(str(model.expenses)),
            employees=model.employees,
            clients=model.clients,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    def _to_model(self, entity: Company) -> CompanyModel:
        return CompanyModel(
            id=entity.id,
            name=entity.name,
            street=entity.street,
            city=entity.city,
            state=entity.state,
            zip_code=entity.zip_code,
            country=entity.country,
            billing=float(entity.billing),
            expenses=float(entity.expenses),
            employees=entity.employees,
            clients=entity.clients,
        )
