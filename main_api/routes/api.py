import asyncio
import logging

from fastapi import APIRouter
from nucliadb_models.search import KnowledgeboxSearchResults

from ..helpers.dataset import load_dataset_by_name, load_model_by_name
from ..types.nuclia_api import NucliaGetOrCreate, NucliaCreated, NucliaSearch, NucliaDelete

logger = logging.getLogger()
api_kb = APIRouter(prefix="/v1/knowledge-box")


async def process_data_set(request: NucliaGetOrCreate):
    dataset = await load_dataset_by_name()
    model = await load_model_by_name()
    request.model = model
    await request.upload_to_knowledge_box(dataset)


@api_kb.post("/create", response_model=None, status_code=200)
async def create_kb(request: NucliaGetOrCreate) -> NucliaCreated:
    asyncio.create_task(process_data_set(request))
    return NucliaCreated(slug=request.slug)


@api_kb.get("/search", response_model=None, status_code=200)
async def search_on_kb(term: str, slug: str) -> KnowledgeboxSearchResults:
    model = await load_model_by_name()

    kb = await NucliaGetOrCreate(slug=slug, model=model).get_or_create_by_slug()

    query = model.encode([term])[0]
    search = await NucliaSearch(term=term).search(query=query, knowledgebox=kb)
    return search.inner_search_results


@api_kb.delete("/delete", status_code=200)
async def delete_kb(slug: str) -> NucliaDelete:
    try:
        delete = NucliaDelete(slug=slug)
        await delete.delete_by_slug()
    except AttributeError:
        logger.warning(f"Knowledgebox id:{slug} does not exists.")
    return delete
