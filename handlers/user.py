import tornado.web
import methods.readdb as mrd
class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        user_infos = mrd.select_table(table="userinfo",column="*",condition="username",value=username),
        print(self.get_secure_cookie(username))
        self.render("user.html", user=user_infos)