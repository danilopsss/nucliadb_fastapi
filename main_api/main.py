from fastapi import FastAPI
from .routes.health_check import main_router
from .routes.api import api_kb

app = FastAPI()
app.include_router(main_router)
app.include_router(api_kb)
