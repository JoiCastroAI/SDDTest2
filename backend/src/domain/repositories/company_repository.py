from abc import ABC, abstractmethod

from src.domain.entities.company import Company
from src.domain.entities.paginated_result import PaginatedResult


class CompanyRepository(ABC):
    @abstractmethod
    async def create(self, company: Company) -> Company: ...

    @abstractmethod
    async def get_by_id(self, company_id: int) -> Company | None: ...

    @abstractmethod
    async def update(self, company: Company) -> Company: ...

    @abstractmethod
    async def delete(self, company_id: int) -> None: ...

    @abstractmethod
    async def find_paginated(
        self,
        page: int = 1,
        page_size: int = 10,
        search: str | None = None,
        sort_by: str = "name",
        sort_order: str = "asc",
    ) -> PaginatedResult[Company]: ...
