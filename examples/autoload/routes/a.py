from fastapi import APIRouter

Router = APIRouter()
RouterParams = dict(
    args=[],
    kwargs=dict(
        prefix='/prefix',
        tags=['A'],
        router=Router,
    ),
)


@Router.get('/a')
async def a():
    return 'a'
