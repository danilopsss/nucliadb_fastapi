from ..main import app
from ..routes.exceptions import ServiceUnavailable


@app.exception_handler(ServiceUnavailable)
async def service_unavailable_exception(request, exc):
    raise ServiceUnavailable(request, exc)
