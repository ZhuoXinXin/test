import tornado.web
import methods.readdb as mrd

class RegistHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("regist.html")
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="userinfo", column="*", condition="username", value=username)
        if user_infos:
            self.write("用户名已存在，请修改用户名")
        else:
            mrd.insert_UserInfo(username,password)
            self.write("注册成功")