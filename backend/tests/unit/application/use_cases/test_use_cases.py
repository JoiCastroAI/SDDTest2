from decimal import Decimal
from unittest.mock import AsyncMock

import pytest

from src.application.use_cases.create_company import CreateCompanyUseCase
from src.application.use_cases.delete_company import DeleteCompanyUseCase
from src.application.use_cases.get_company import GetCompanyUseCase
from src.application.use_cases.list_companies import ListCompaniesUseCase
from src.application.use_cases.update_company import UpdateCompanyUseCase
from src.domain.entities.company import Company
from src.domain.entities.paginated_result import PaginatedResult
from src.domain.exceptions import NotFoundError


def _make_company(**kwargs: object) -> Company:
    defaults = dict(
        id=1,
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


class TestCreateCompanyUseCase:
    @pytest.fixture
    def mock_repo(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def use_case(self, mock_repo: AsyncMock) -> CreateCompanyUseCase:
        return CreateCompanyUseCase(mock_repo)

    async def test_should_create_company_when_valid_data(
        self, use_case: CreateCompanyUseCase, mock_repo: AsyncMock
    ) -> None:
        company = _make_company(id=None)
        mock_repo.create.return_value = _make_company()

        result = await use_case.execute(company)

        assert result.id == 1
        mock_repo.create.assert_called_once_with(company)


class TestGetCompanyUseCase:
    @pytest.fixture
    def mock_repo(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def use_case(self, mock_repo: AsyncMock) -> GetCompanyUseCase:
        return GetCompanyUseCase(mock_repo)

    async def test_should_return_company_when_exists(
        self, use_case: GetCompanyUseCase, mock_repo: AsyncMock
    ) -> None:
        mock_repo.get_by_id.return_value = _make_company()

        result = await use_case.execute(1)

        assert result.id == 1
        assert result.name == "Acme Corp"

    async def test_should_raise_not_found_when_missing(
        self, use_case: GetCompanyUseCase, mock_repo: AsyncMock
    ) -> None:
        mock_repo.get_by_id.return_value = None

        with pytest.raises(NotFoundError, match="Company not found: 999"):
            await use_case.execute(999)


class TestListCompaniesUseCase:
    @pytest.fixture
    def mock_repo(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def use_case(self, mock_repo: AsyncMock) -> ListCompaniesUseCase:
        return ListCompaniesUseCase(mock_repo)

    async def test_should_return_paginated_results(
        self, use_case: ListCompaniesUseCase, mock_repo: AsyncMock
    ) -> None:
        expected = PaginatedResult(items=[_make_company()], total=1, page=1, page_size=10)
        mock_repo.find_paginated.return_value = expected

        result = await use_case.execute(page=1, page_size=10)

        assert result.total == 1
        assert len(result.items) == 1
        mock_repo.find_paginated.assert_called_once()


class TestUpdateCompanyUseCase:
    @pytest.fixture
    def mock_repo(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def use_case(self, mock_repo: AsyncMock) -> UpdateCompanyUseCase:
        return UpdateCompanyUseCase(mock_repo)

    async def test_should_update_company_when_exists(
        self, use_case: UpdateCompanyUseCase, mock_repo: AsyncMock
    ) -> None:
        mock_repo.get_by_id.return_value = _make_company()
        updated = _make_company(name="Updated Corp")
        mock_repo.update.return_value = updated

        result = await use_case.execute(1, _make_company(name="Updated Corp", id=None))

        assert result.name == "Updated Corp"
        mock_repo.update.assert_called_once()

    async def test_should_raise_not_found_when_updating_missing(
        self, use_case: UpdateCompanyUseCase, mock_repo: AsyncMock
    ) -> None:
        mock_repo.get_by_id.return_value = None

        with pytest.raises(NotFoundError, match="Company not found: 999"):
            await use_case.execute(999, _make_company(id=None))


class TestDeleteCompanyUseCase:
    @pytest.fixture
    def mock_repo(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def use_case(self, mock_repo: AsyncMock) -> DeleteCompanyUseCase:
        return DeleteCompanyUseCase(mock_repo)

    async def test_should_delete_company_when_exists(
        self, use_case: DeleteCompanyUseCase, mock_repo: AsyncMock
    ) -> None:
        mock_repo.get_by_id.return_value = _make_company()

        await use_case.execute(1)

        mock_repo.delete.assert_called_once_with(1)

    async def test_should_raise_not_found_when_deleting_missing(
        self, use_case: DeleteCompanyUseCase, mock_repo: AsyncMock
    ) -> None:
        mock_repo.get_by_id.return_value = None

        with pytest.raises(NotFoundError, match="Company not found: 999"):
            await use_case.execute(999)
