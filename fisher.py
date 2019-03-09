from flask import Flask, make_response

app = Flask(__name__)


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html><html>', 404)
    response.headers = headers
    return response


def helloo():
    return 'hello , flask'


# app.add_url_rule('/hello', view_func=hello)

# 生产环境nginx+uwsgi
if __name__ == '__main__':
    app.run()
