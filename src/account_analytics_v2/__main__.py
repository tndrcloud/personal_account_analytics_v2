import uvicorn
from .settings import settings


uvicorn.run(
    'account_analytics_v2.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)
