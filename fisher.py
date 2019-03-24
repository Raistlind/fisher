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


# app.add_url_rule('/hello', view_func=hello)
from app import create_app

app = create_app()

# 生产环境nginx+uwsgi
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
    # 可加参数 threaded=True 多线程
    # 可加参数 processes=1 多进程， 数字代表进程数
