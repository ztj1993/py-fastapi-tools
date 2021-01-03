from fastapi import APIRouter

Router = APIRouter()


@Router.get('/b')
async def b():
    return 'b'
