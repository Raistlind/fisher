#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   base.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time          @Author      @Version    @Description
-----------------     ---------    --------    -----------
2019-04-01 23:03      RaistlinD    1.0         None
"""

# import lib
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


if __name__ == '__main__':
    pass
