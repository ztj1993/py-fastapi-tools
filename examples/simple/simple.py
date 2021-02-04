from fastapi import FastAPI

from ZtjFastApiRoute import Router
from ZtjFastApiServe import FastApiServe
from ZtjFastApiTool import FastApiTool

api = FastAPI(title='示例项目')

tool = FastApiTool(api)
tool.include_route(Router)

if __name__ == '__main__':
    FastApiServe('simple:api').local()
