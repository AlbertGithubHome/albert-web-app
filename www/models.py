#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Models for user, blog, comment

__author__ = 'Albert Shi'

import time, uuid
from orm import Model, StringField, FloatField, TextField, BooleanField

# WHAT?
def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.iuuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(64)')
    email = StringField(ddl='varchar(64)')
    password = StringField(ddl='varchar(64)')
    admin = BooleanField()
    name = StringField(ddl='varchar(64)')
    image = StringField(ddl='varchar(640)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'bolgs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(64)')
    user_id = StringField(ddl='varchar(64)')
    user_name = StringField(ddl='varchar(64)')
    user_image = StringField(ddl='varchar(64)')
    name = StringField(ddl='varchar(64)')
    summary = StringField(ddl='varchar(256)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(64)')
    blog_id = StringField(ddl='varchar(64)')
    user_id = StringField(ddl='varchar(64)')
    user_name = StringField(ddl='varchar(64)')
    user_image = StringField(ddl='varchar(64)')
    content = TextField()
    created_at = FloatField(default=time.time)
