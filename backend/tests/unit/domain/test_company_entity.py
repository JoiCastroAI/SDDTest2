from decimal import Decimal

import pytest

from src.domain.entities.company import Company


class TestCompanyEntity:
    """Tests for Company entity."""

    def test_should_compute_profit_when_billing_exceeds_expenses(self) -> None:
        company = Company(
            name="Acme",
            street="123 Main",
            city="Springfield",
            state="IL",
            zip_code="62701",
            country="US",
            billing=Decimal("50000"),
            expenses=Decimal("30000"),
        )
        assert company.profit == Decimal("20000")

    def test_should_compute_negative_profit_when_expenses_exceed_billing(self) -> None:
        company = Company(
            name="Acme",
            street="123 Main",
            city="Springfield",
            state="IL",
            zip_code="62701",
            country="US",
            billing=Decimal("10000"),
            expenses=Decimal("30000"),
        )
        assert company.profit == Decimal("-20000")

    def test_should_compute_zero_profit_when_billing_equals_expenses(self) -> None:
        company = Company(
            name="Acme",
            street="123 Main",
            city="Springfield",
            state="IL",
            zip_code="62701",
            country="US",
            billing=Decimal("5000"),
            expenses=Decimal("5000"),
        )
        assert company.profit == Decimal("0")

    def test_should_create_entity_with_all_required_fields(self) -> None:
        company = Company(
            name="Test Corp",
            street="456 Oak Ave",
            city="Austin",
            state="TX",
            zip_code="73301",
            country="US",
            billing=Decimal("100000"),
            expenses=Decimal("50000"),
            employees=50,
            clients=20,
        )
        assert company.name == "Test Corp"
        assert company.street == "456 Oak Ave"
        assert company.city == "Austin"
        assert company.state == "TX"
        assert company.zip_code == "73301"
        assert company.country == "US"
        assert company.employees == 50
        assert company.clients == 20
        assert company.id is None

    def test_should_have_default_values_for_optional_fields(self) -> None:
        company = Company(
            name="Minimal",
            street="1 St",
            city="City",
            state="ST",
            zip_code="00000",
            country="US",
        )
        assert company.billing == Decimal("0")
        assert company.expenses == Decimal("0")
        assert company.employees == 0
        assert company.clients == 0


class TestPaginatedResult:
    """Tests for PaginatedResult."""

    def test_should_compute_total_pages_evenly(self) -> None:
        from src.domain.entities.paginated_result import PaginatedResult

        result: PaginatedResult[str] = PaginatedResult(items=[], total=30, page=1, page_size=10)
        assert result.total_pages == 3

    def test_should_compute_total_pages_with_remainder(self) -> None:
        from src.domain.entities.paginated_result import PaginatedResult

        result: PaginatedResult[str] = PaginatedResult(items=[], total=25, page=1, page_size=10)
        assert result.total_pages == 3

    def test_should_return_zero_total_pages_when_empty(self) -> None:
        from src.domain.entities.paginated_result import PaginatedResult

        result: PaginatedResult[str] = PaginatedResult(items=[], total=0, page=1, page_size=10)
        assert result.total_pages == 0
