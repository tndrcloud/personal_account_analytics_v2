from fastapi import FastAPI
from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authorization and authentication'
    },
    {
        'name': 'operations',
        'description': 'Operations'
    },
]


app = FastAPI(
    title='Personal Account Analytics',
    description='Cервис для проверки корректности настроек и поиска ошибок в логах вызовов ЛК ВАТС',
    version='v2',
    openapi_tags=tags_metadata
)
app.include_router(router)
