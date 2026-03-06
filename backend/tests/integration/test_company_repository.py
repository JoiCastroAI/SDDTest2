from decimal import Decimal

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.company import Company
from src.infrastructure.database.repositories.company_repo import SqlAlchemyCompanyRepository


def _make_company(**kwargs: object) -> Company:
    defaults = dict(
        name="Acme Corp",
        street="123 Main",
        city="Springfield",
        state="IL",
        zip_code="62701",
        country="US",
        billing=Decimal("50000"),
        expenses=Decimal("30000"),
        employees=10,
        clients=5,
    )
    defaults.update(kwargs)
    return Company(**defaults)  # type: ignore[arg-type]


class TestSqlAlchemyCompanyRepository:
    @pytest.fixture
    def repo(self, async_session: AsyncSession) -> SqlAlchemyCompanyRepository:
        return SqlAlchemyCompanyRepository(async_session)

    async def test_should_create_and_retrieve_company(
        self, repo: SqlAlchemyCompanyRepository
    ) -> None:
        company = _make_company()
        created = await repo.create(company)

        assert created.id is not None
        assert created.name == "Acme Corp"

        fetched = await repo.get_by_id(created.id)
        assert fetched is not None
        assert fetched.name == "Acme Corp"

    async def test_should_return_none_for_nonexistent_id(
        self, repo: SqlAlchemyCompanyRepository
    ) -> None:
        result = await repo.get_by_id(999)
        assert result is None

    async def test_should_update_company(self, repo: SqlAlchemyCompanyRepository) -> None:
        created = await repo.create(_make_company())
        assert created.id is not None

        created.name = "Updated Corp"
        updated = await repo.update(created)

        assert updated.name == "Updated Corp"

    async def test_should_delete_company(self, repo: SqlAlchemyCompanyRepository) -> None:
        created = await repo.create(_make_company())
        assert created.id is not None

        await repo.delete(created.id)
        result = await repo.get_by_id(created.id)
        assert result is None

    async def test_should_paginate_results(self, repo: SqlAlchemyCompanyRepository) -> None:
        for i in range(25):
            await repo.create(_make_company(name=f"Company {i:02d}"))

        result = await repo.find_paginated(page=2, page_size=10)

        assert len(result.items) == 10
        assert result.total == 25
        assert result.page == 2
        assert result.page_size == 10
        assert result.total_pages == 3

    async def test_should_search_by_name(self, repo: SqlAlchemyCompanyRepository) -> None:
        await repo.create(_make_company(name="Acme Corp"))
        await repo.create(_make_company(name="Beta Inc"))

        result = await repo.find_paginated(search="acme")

        assert result.total == 1
        assert result.items[0].name == "Acme Corp"

    async def test_should_sort_by_name_ascending(
        self, repo: SqlAlchemyCompanyRepository
    ) -> None:
        await repo.create(_make_company(name="Zeta"))
        await repo.create(_make_company(name="Alpha"))

        result = await repo.find_paginated(sort_by="name", sort_order="asc")

        assert result.items[0].name == "Alpha"
        assert result.items[1].name == "Zeta"

    async def test_should_sort_by_name_descending(
        self, repo: SqlAlchemyCompanyRepository
    ) -> None:
        await repo.create(_make_company(name="Alpha"))
        await repo.create(_make_company(name="Zeta"))

        result = await repo.find_paginated(sort_by="name", sort_order="desc")

        assert result.items[0].name == "Zeta"
        assert result.items[1].name == "Alpha"
