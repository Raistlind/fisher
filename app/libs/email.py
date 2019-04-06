#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   email.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-06 09:45      RaistlinD    1.0         None
"""

# import lib
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail


# # Email配置
# MAIL_SERVER = 'smtp.163.com'
# MAIL_PORT = 465
# MAIL_USE_SSL = True
# MAIL_USE_TSL = False
# MAIL_USERNAME = 'jojo@163.com'
# MAIL_PASSWORD = 'abc' QQ邮件提供授权码
# MAIL_SUBJECT_PREFIX = '[FISHER]'
# MAIL_SENDER = 'FISHER <jojo@163.com>'

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='jojo@163.com', body='Test', recipients=['user@qq.com', 'user2@qq.com'])
    msg = Message('[鱼书 ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()


if __name__ == '__main__':
    pass
