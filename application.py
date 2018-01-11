# coding:utf-8
from url import url

import tornado.web
import os

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics"),
    cookie_secret='jeZs7k2bSFG/MSe2mMNqaw==',
    srf_cookies=True
)
application = tornado.web.Application(
    handlers=url,
    **settings
)
