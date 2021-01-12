# -*- coding: utf-8 -*-
# Intro: FastApi 路由
# Author: Ztj
# Email: ztj1993@gmail.com

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

Router = APIRouter()


@Router.get('/health', response_class=PlainTextResponse)
async def health():
    """服务状态"""
    return 'ok'
