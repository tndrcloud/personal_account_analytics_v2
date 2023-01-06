from fastapi import FastAPI
from .api import router


tags_metadata = [
    {
        'name': 'Authorization and authentication',
    },
    {
        'name': 'Operations',
    },
]


app = FastAPI(
    title='Анализатор ЛК ВАТС',
    description='REST API сервис для проверки корректности настроек и поиска ошибок в логах вызовов ЛК ВАТС',
    version='v2.0',
    openapi_tags=tags_metadata
)
app.include_router(router)
