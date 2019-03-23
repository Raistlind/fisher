import json

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


# app.add_url_rule('/hello', view_func=hello)

# 生产环境nginx+uwsgi
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

#
#