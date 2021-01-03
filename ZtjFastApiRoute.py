# -*- coding: utf-8 -*-
# Intro: FastApi 路由
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2020-01-03

from fastapi import APIRouter

Router = APIRouter()


@Router.get('/health')
async def health():
    """服务状态"""
    return 'ok'
