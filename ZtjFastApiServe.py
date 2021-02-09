# -*- coding: utf-8 -*-
# Intro: FastApi 服务
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2020-01-03

import os

import uvicorn
from get_port import get_port


class FastApiServe(object):
    """接口服务"""

    def __init__(self, app):
        self.app = app
        self.host = os.getenv('HOST', '0.0.0.0')
        self.port = int(os.getenv('PORT', 80))

    def production(self, **kwargs):
        """运行应用"""
        uvicorn.run(
            self.app,
            host=self.host,
            port=self.port,
            access_log=True,
            **kwargs
        )

    def development(self, **kwargs):
        """运行应用"""
        uvicorn.run(
            self.app,
            host=self.host,
            port=get_port(self.port),
            reload=True,
            debug=True,
            access_log=True,
            **kwargs
        )

    def local(self, **kwargs):
        """运行应用"""
        uvicorn.run(
            self.app,
            host='127.0.0.1',
            port=get_port(80),
            reload=True,
            access_log=True,
            debug=True,
            **kwargs
        )
