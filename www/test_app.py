#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is a test file for app

import orm
from models import User, Blog, Comment

def test():
    await orm.create_pool(None, user='albertwebapp', password='123456', database='web_app')

    u = User(name='Test', email='test@example.com', password='12345678', image='about:blank')

    await u.save()

for x in test():
    pass