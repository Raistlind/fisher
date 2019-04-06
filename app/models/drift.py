#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   drift.py
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-06 16:47      RaistlinD    1.0         None
"""

# import lib
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base


class Drift(Base):
    id = Column(Integer, primary_key=True)

    # 邮寄者信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    # 鱼漂状态
    pending = Column('pending', SmallInteger, default=1)
