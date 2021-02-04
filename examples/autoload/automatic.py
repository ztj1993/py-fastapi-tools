from fastapi import FastAPI

import routes
from ZtjFastApiRoute import Router
from ZtjFastApiServe import FastApiServe
from ZtjFastApiTool import FastApiTool

api = FastAPI(title='自动加载路由示例项目')

tool = FastApiTool(api)
tool.include_route(Router)
tool.load_routes(routes.__path__)

if __name__ == '__main__':
    FastApiServe('automatic:api').local()
