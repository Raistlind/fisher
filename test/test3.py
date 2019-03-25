#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test3.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Desciption
-----------------    ---------    --------    -----------
2019-03-25 22:48      Raistlind    1.0         None
"""

# import lib
from werkzeug.local import LocalStack

s = LocalStack()

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

if __name__ == '__main__':
    pass
