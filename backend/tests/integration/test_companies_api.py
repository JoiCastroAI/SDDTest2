from decimal import Decimal

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.infrastructure.database.base import Base
from src.infrastructure.database.session import get_session
from src.main import app


@pytest.fixture
async def test_session() -> AsyncSession:
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with session_factory() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest.fixture
async def client(test_session: AsyncSession) -> AsyncClient:
    async def override_session():  # type: ignore[no-untyped-def]
        try:
            yield test_session
            await test_session.commit()
        except Exception:
            await test_session.rollback()
            raise

    app.dependency_overrides[get_session] = override_session
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


VALID_COMPANY = {
    "name": "Acme Corp",
    "street": "123 Main",
    "city": "Springfield",
    "state": "IL",
    "zip_code": "62701",
    "country": "US",
    "billing": 50000,
    "expenses": 30000,
    "employees": 10,
    "clients": 5,
}


class TestCompaniesApi:
    async def test_should_create_company(self, client: AsyncClient) -> None:
        response = await client.post("/api/v1/companies/", json=VALID_COMPANY)

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Acme Corp"
        assert data["profit"] == 20000
        assert data["id"] is not None

    async def test_should_list_companies(self, client: AsyncClient) -> None:
        await client.post("/api/v1/companies/", json=VALID_COMPANY)

        response = await client.get("/api/v1/companies/")

        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert len(data["items"]) == 1

    async def test_should_get_company_by_id(self, client: AsyncClient) -> None:
        create_resp = await client.post("/api/v1/companies/", json=VALID_COMPANY)
        company_id = create_resp.json()["id"]

        response = await client.get(f"/api/v1/companies/{company_id}")

        assert response.status_code == 200
        assert response.json()["name"] == "Acme Corp"

    async def test_should_return_404_for_nonexistent_company(self, client: AsyncClient) -> None:
        response = await client.get("/api/v1/companies/999")

        assert response.status_code == 404
        assert response.json()["error"]["code"] == "NOT_FOUND"

    async def test_should_update_company(self, client: AsyncClient) -> None:
        create_resp = await client.post("/api/v1/companies/", json=VALID_COMPANY)
        company_id = create_resp.json()["id"]

        updated_data = {**VALID_COMPANY, "name": "Updated Corp"}
        response = await client.put(f"/api/v1/companies/{company_id}", json=updated_data)

        assert response.status_code == 200
        assert response.json()["name"] == "Updated Corp"

    async def test_should_delete_company(self, client: AsyncClient) -> None:
        create_resp = await client.post("/api/v1/companies/", json=VALID_COMPANY)
        company_id = create_resp.json()["id"]

        response = await client.delete(f"/api/v1/companies/{company_id}")

        assert response.status_code == 204

        get_resp = await client.get(f"/api/v1/companies/{company_id}")
        assert get_resp.status_code == 404

    async def test_should_return_422_for_invalid_data(self, client: AsyncClient) -> None:
        response = await client.post("/api/v1/companies/", json={"name": ""})

        assert response.status_code == 422

    async def test_should_return_404_when_updating_nonexistent(self, client: AsyncClient) -> None:
        response = await client.put("/api/v1/companies/999", json=VALID_COMPANY)

        assert response.status_code == 404

    async def test_should_return_404_when_deleting_nonexistent(self, client: AsyncClient) -> None:
        response = await client.delete("/api/v1/companies/999")

        assert response.status_code == 404
