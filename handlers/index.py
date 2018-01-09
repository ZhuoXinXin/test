# coding:utf-8
import tornado.web
import tornado.escape
import methods.readdb as mrd
from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        # usernames = mrd.select_columns(table="userinfo",column="username")
        # one_user = usernames[0][0]
        self.render("index.html")  # ,user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="userinfo", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][1]
            if db_pwd == password:
                # self.set_cookie(username,db_pwd)
                self.set_current_user(username)
                self.write("welcome!")
            else:
                self.write("密码或者用户名错误")
        else:
            self.write("密码或者用户名错误")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode())
        else:
            self.clear_cookie()

class ErrorHandler(BaseHandler):
    def get(self):
        self.render("error.html")