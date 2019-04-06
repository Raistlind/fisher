#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   enums.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-06 17:24      RaistlinD    1.0         None
"""

# import lib

from enum import Enum


class PendingStatus(Enum):
    WAITING = 1
    SUCCESS = 2
    REJECT = 3
    REDRAW = 4

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            1: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            3: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            4: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            },
            2: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄，交易完成'
            }
        }
        return key_map[status][key]