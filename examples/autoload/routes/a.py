from fastapi import APIRouter

Router = APIRouter()


@Router.get('/a')
async def a():
    return 'a'
