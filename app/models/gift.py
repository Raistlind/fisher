#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   gift.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time          @Author      @Version    @Description
-----------------     ---------    --------    -----------
2019-04-01 23:01      RaistlinD    1.0         None
"""

# import lib
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(
            Gift.create_datetime).limit(current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift


if __name__ == '__main__':
    pass
