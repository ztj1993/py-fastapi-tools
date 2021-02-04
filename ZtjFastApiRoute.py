# -*- coding: utf-8 -*-
# Intro: FastApi 路由
# Author: Ztj
# Email: ztj1993@gmail.com

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

Router = APIRouter()


@Router.get('/health', name='服务状态', response_class=PlainTextResponse)
async def health():
    return 'ok'
