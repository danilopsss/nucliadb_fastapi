import os
from numpy import ndarray
from pydantic import BaseModel
from typing import List, Optional
from nucliadb_sdk.search import SearchResult
from nucliadb_sdk import KnowledgeBox, get_or_create, delete_kb
from sentence_transformers import SentenceTransformer


class NucliaEndpoints:
    ROOT: str = os.environ.get("NUCLIA_HOST", "nuclia-db")
    PORT: str = os.environ.get("NUCLIA_PORT", "8080")
    PROTOCOL: str = os.environ.get("NUCLIA_PORT", "http://")


class NucliaCreated(BaseModel):
    slug: str


class NucliaGetOrCreate(BaseModel):
    slug: str
    model: Optional[SentenceTransformer]

    class Config:
        arbitrary_types_allowed = True

    async def get_or_create_by_slug(self) -> KnowledgeBox:
        nuclia_url = "{}{}:{}".format(NucliaEndpoints.PROTOCOL, NucliaEndpoints.ROOT, NucliaEndpoints.PORT)
        return get_or_create(self.slug, nucliadb_base_url=nuclia_url)

    async def upload_to_knowledge_box(self, dataset: List[dict]) -> None:
        knowledge_box = await self.get_or_create_by_slug()
        for item in dataset["train"]:
            prompt = item["prompt"]
            knowledge_box.upload(text=prompt, vectors={"ms-marco-vectors": self.model.encode([prompt])[0]})


class NucliaDelete(BaseModel):
    slug: str

    async def delete_by_slug(self) -> KnowledgeBox:
        nuclia_url = "{}{}:{}".format(NucliaEndpoints.PROTOCOL, NucliaEndpoints.ROOT, NucliaEndpoints.PORT)
        return delete_kb(self.slug, nucliadb_base_url=nuclia_url)


class NucliaSearch(BaseModel):
    term: str

    async def search(self, query: ndarray, knowledgebox: KnowledgeBox) -> SearchResult:
        return knowledgebox.search(vector=query, vectorset="ms-marco-vectors", min_score=0.35)
