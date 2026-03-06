from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal


@dataclass
class Company:
    name: str
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    billing: Decimal = Decimal("0")
    expenses: Decimal = Decimal("0")
    employees: int = 0
    clients: int = 0
    id: int | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def profit(self) -> Decimal:
        return self.billing - self.expenses
