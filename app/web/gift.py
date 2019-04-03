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
from flask import current_app
from flask_login import login_required, current_user

from app import db
from app.models.gift import Gift
from . import web



@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit()

    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



