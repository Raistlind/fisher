#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   user.py
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time          @Author      @Version    @Description
-----------------     ---------    --------    -----------
2019-04-02 10:01      RaistlinD    1.0         None
"""

# import lib
from flask_login import login_required

from . import web



@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



