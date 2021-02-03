# -*- coding: utf-8 -*-
# Intro: FastApi 应用
# Author: Ztj
# Email: ztj1993@gmail.com

from ZtjDirImport import DirImport
from fastapi import APIRouter
from fastapi import FastAPI


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
        if isinstance(route, dict):
            self.get_fast_api().include_router(
                *route.get('args', []),
                **route.get('kwargs', []),
            )
        elif isinstance(route, APIRouter):
            self.get_fast_api().include_router(route)

    def load_routes(self, directory):
        """加载路由"""
        routes = []
        modules = DirImport('routes', directory).all()
        for name, module in modules.items():
            if hasattr(module, 'RouterParams'):
                route = getattr(module, 'RouterParams')
                if isinstance(route, dict):
                    routes.append(route)
            elif hasattr(module, 'Router'):
                route = getattr(module, 'Router')
                if isinstance(route, APIRouter):
                    routes.append(route)
        self.include_routes(routes)
