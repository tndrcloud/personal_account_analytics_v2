from fastapi import FastAPI
from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и аутентификация'
    },
    {
        'name': 'operations',
        'description': 'Work with operations'
    },
]


app = FastAPI(
    title='Анализатор ЛК ВАТС',
    description='REST API сервис для проверки корректности настроек и поиска ошибок в логах вызовов ЛК ВАТС',
    version='v2.0',
    openapi_tags=tags_metadata
)
app.include_router(router)
