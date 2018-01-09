# coding=utf-8

import sys

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.regist import RegistHandler

url = [
    (r'/', IndexHandler),
    (r'/login', IndexHandler),
    (r'/user', UserHandler),
    (r'/regist', RegistHandler)
]