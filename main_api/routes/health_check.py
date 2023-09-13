from fastapi import APIRouter
from ..helpers.service_checker import evaluate_service_health

main_router = APIRouter(prefix="/internal")


@main_router.head("/health", status_code=200)
async def health_check() -> None:
    evaluate_service_health("nuclia_db")
    return
