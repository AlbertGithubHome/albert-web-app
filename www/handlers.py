#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# url handler

__author__ = 'Albert Shi'

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post
from models import User, Comment, Blog, next_id

@get('/test')
async def test(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

@get('/blog')
async def blog(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs,
        '__flag__': 1
    }

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'index.html',
        'users': users
    }

@get('/tutorial')
async def tutorial(request):
    users = await User.findAll()
    return {
        '__template__': 'tutorial.html',
        'users': users,
        '__flag__': 2
    }

@get('/api/allusers')
async def api_get_users(request):
    users = await User.findAll(orderBy='created_at desc')
    for u in users:
        u.password = '******'
    return dict(users=users)