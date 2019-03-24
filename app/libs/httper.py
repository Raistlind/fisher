#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   httper.py
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time      @Author      @Version    @Desciption
------------      ---------    --------    -----------
2019-03-09 22:19   Raistlind      1.0         None
"""

# import lib
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text()
