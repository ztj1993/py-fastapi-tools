# -*- coding: utf-8 -*-
# Intro: FastApi 模块
# Author: Ztj
# Email: ztj1993@gmail.com

import os.path

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

setup(
    name='fastapi-tools',
    version='0.0.3',
    description='fastapi tools',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['ZtjFastApiTool', 'ZtjFastApiRoute', 'ZtjFastApiServe'],
    url='https://github.com/ztj1993/py-fastapi-tools',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='fastapi',
    license='MIT License',
    install_requires=[
        'uvicorn',
        'fastapi',
        'get-port',
        'dir-import==0.0.3',
    ],
)
