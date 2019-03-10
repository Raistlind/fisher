from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    response = make_response('<html><html>', 404)
    response.headers = headers
    return response


@app.route('/book/search/<q>/<page>')
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
    return result


# app.add_url_rule('/hello', view_func=hello)

# 生产环境nginx+uwsgi
if __name__ == '__main__':
    app.run()
