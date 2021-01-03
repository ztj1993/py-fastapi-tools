# -*- coding: utf-8 -*-
# Intro: FastApi 应用
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2020-01-03

from fastapi import FastAPI, APIRouter

from ZtjDirImport import DirImport


class FastApiApp(object):
    """接口应用"""

    def __init__(self):
        self.fast_api = None
        self.routes = None

    def get_fast_api(self):
        """获取应用"""
        if self.fast_api is None:
            self.fast_api = FastAPI()
        return self.fast_api

    def include_routes(self, routes):
        """包含路由"""
        for route in routes:
            self.include_route(route)

    def include_route(self, route):
        """包含路由"""
        self.get_fast_api().include_router(route)

    def load_routes(self, directory):
        """加载路由"""
        routes = []
        modules = DirImport('routes', directory).all()
        for name, module in modules.items():
            if not hasattr(module, 'Router'):
                continue
            route = getattr(module, 'Router')
            if not isinstance(route, APIRouter):
                continue
            routes.append(route)
        self.include_routes(routes)
