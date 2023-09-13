from datasets import load_dataset
from datasets.dataset_dict import DatasetDict
from sentence_transformers import SentenceTransformer


async def load_dataset_by_name(ds_name: str = None) -> DatasetDict:
    if not ds_name:
        ds_name = "fka/awesome-chatgpt-prompts"
    return load_dataset(ds_name)


async def load_model_by_name(model_name: str = None) -> SentenceTransformer:
    if not model_name:
        model_name = "sentence-transformers/msmarco-MiniLM-L6-cos-v5"
    return SentenceTransformer(model_name)
