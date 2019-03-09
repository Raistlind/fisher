from flask import Flask, make_response

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
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'

    short_q = q.replace('-', '')

    if '-' in q and len(short_q) == 10 and short_q.isdigit:
        isbn_or_key = 'isbn'

    return 'hello , flask'


# app.add_url_rule('/hello', view_func=hello)

# 生产环境nginx+uwsgi
if __name__ == '__main__':
    app.run()
