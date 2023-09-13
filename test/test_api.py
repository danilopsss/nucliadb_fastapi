import pytest
import pytest_asyncio
from httpx import AsyncClient
from main_api.main import app


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_create_kb(client):
    request_data = {
        "slug": "test_slug",
    }
    response = await client.post("/v1/knowledge-box/create", json=request_data)
    assert response.status_code == 200
    assert response.json() == {"slug": "test_slug"}


@pytest.mark.asyncio
async def test_search_on_kb(client):
    term = "test_term"
    slug = "test_slug"
    response = await client.get(f"/v1/knowledge-box/search?term={term}&slug={slug}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_kb(client):
    slug = "test_slug"
    response = await client.delete(f"/v1/knowledge-box/delete?slug={slug}")
    assert response.status_code == 200
