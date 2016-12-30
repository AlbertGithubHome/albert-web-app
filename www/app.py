#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Web start

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Hello, Albert!</h1>', content_type='text/html', charset='UTF-8')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9106)
    logging.info('server started at http://127.0.0.1:9106...')
    return srv

def start_server():
    main_loop = asyncio.get_event_loop()
    main_loop.run_until_complete(init(main_loop))
    main_loop.run_forever()

if __name__ == '__main__':
    start_server()