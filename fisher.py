from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello , flask'


def helloo():
    return 'hello , flask'


# app.add_url_rule('/hello', view_func=hello)

# 生产环境nginx+uwsgi
if __name__ == '__main__':
    app.run()
