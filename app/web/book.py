#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   book.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Desciption
-----------------    ---------    --------    -----------
2019-03-23 21:10      Raistlind    1.0         None
"""

# import lib
from flask import jsonify

from app.web.blueprint import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q:普通关键字、ISBN
        page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}


if __name__ == '__main__':
    pass
