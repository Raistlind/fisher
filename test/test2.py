#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test2.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Desciption
-----------------    ---------    --------    -----------
2019-03-25 22:33      Raistlind    1.0         None
"""
import threading
import time

from werkzeug.local import Local


# Local使用字典的方式实现的线程隔离
# LocalStack 线程隔离的栈结构


class A():
    b = 1


my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print('worker thread ' + str(my_obj.b))


new_t = threading.Thread(target=worker, name="dq's thread")

new_t.start()
time.sleep(1)
print('main thread ' + str(my_obj.b))
