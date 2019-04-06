#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   secure.py
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Desciption
-----------------    ---------    --------    -----------
2019-03-23 21:12      Raistlind    1.0         None
"""

# import lib

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:8889/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = 'adedfefdgrgdw'

# Email配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'jojo@163.com'
MAIL_PASSWORD = 'abc'
MAIL_SUBJECT_PREFIX = '[FISHER]'
MAIL_SENDER = 'FISHER <jojo@163.com>'
