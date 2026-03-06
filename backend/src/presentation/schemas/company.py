from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from src.domain.entities.company import Company


class CreateCompanyRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    street: str = Field(..., min_length=1, max_length=255)
    city: str = Field(..., min_length=1, max_length=100)
    state: str = Field(..., min_length=1, max_length=100)
    zip_code: str = Field(..., min_length=1, max_length=20)
    country: str = Field(..., min_length=1, max_length=100)
    billing: Decimal = Field(default=Decimal("0"), ge=0)
    expenses: Decimal = Field(default=Decimal("0"), ge=0)
    employees: int = Field(default=0, ge=0)
    clients: int = Field(default=0, ge=0)

    def to_entity(self) -> Company:
        return Company(
            name=self.name,
            street=self.street,
            city=self.city,
            state=self.state,
            zip_code=self.zip_code,
            country=self.country,
            billing=self.billing,
            expenses=self.expenses,
            employees=self.employees,
            clients=self.clients,
        )


class UpdateCompanyRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    street: str = Field(..., min_length=1, max_length=255)
    city: str = Field(..., min_length=1, max_length=100)
    state: str = Field(..., min_length=1, max_length=100)
    zip_code: str = Field(..., min_length=1, max_length=20)
    country: str = Field(..., min_length=1, max_length=100)
    billing: Decimal = Field(default=Decimal("0"), ge=0)
    expenses: Decimal = Field(default=Decimal("0"), ge=0)
    employees: int = Field(default=0, ge=0)
    clients: int = Field(default=0, ge=0)

    def to_entity(self) -> Company:
        return Company(
            name=self.name,
            street=self.street,
            city=self.city,
            state=self.state,
            zip_code=self.zip_code,
            country=self.country,
            billing=self.billing,
            expenses=self.expenses,
            employees=self.employees,
            clients=self.clients,
        )


class CompanyResponse(BaseModel):
    id: int
    name: str
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    billing: Decimal
    expenses: Decimal
    profit: Decimal
    employees: int
    clients: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity: Company) -> "CompanyResponse":
        return cls(
            id=entity.id,  # type: ignore[arg-type]
            name=entity.name,
            street=entity.street,
            city=entity.city,
            state=entity.state,
            zip_code=entity.zip_code,
            country=entity.country,
            billing=entity.billing,
            expenses=entity.expenses,
            profit=entity.profit,
            employees=entity.employees,
            clients=entity.clients,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


class PaginatedCompanyResponse(BaseModel):
    items: list[CompanyResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
