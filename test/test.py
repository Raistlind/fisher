#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Desciption
-----------------    ---------    --------    -----------
2019-03-24 17:28      Raistlind    1.0         None
"""

# import lib
from flask import Flask, current_app

app = Flask(__name__)
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

if __name__ == '__main__':
    pass
