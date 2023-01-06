from fastapi import FastAPI
from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authorization and authentication'
    },
    {
        'name': 'operations',
        'description': 'Work with operations'
    },
]


app = FastAPI(
    title='Workshop',
    description='Service private finance data',
    version='v2.0',
    openapi_tags=tags_metadata
)
app.include_router(router)
