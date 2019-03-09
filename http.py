#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   http.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time      @Author      @Version    @Desciption
------------      ---------    --------    -----------
2019-03-09 22:19   Raistlind      1.0         None
'''

# import lib
import requests

class HTTP:
    def get(self, url, return_json=True):
        r = requests.get(url)
        return r
