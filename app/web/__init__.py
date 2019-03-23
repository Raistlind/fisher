#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Desciption
-----------------    ---------    --------    -----------
2019-03-23 22:54      Raistlind    1.0         None
"""

# import lib
from flask import Blueprint

web = Blueprint('web', __name__)

from . import book, user

if __name__ == '__main__':
    pass
