import page
from base.base_login import Base


class Pagelogin(Base):
    '''
    点击登录模块
    输入用户名
    输入密码
    输入验证码
    点击登录
    验证是否成功
    '''
    def page_register(self):
        self.base_click(page.click_login)
    def page_username(self,username):
        self.base_input(page.username_input,username)
    def page_password(self,pwd):
        self.base_input(page.password_input,pwd)
    def page_code(self,answer=8888):
        self.base_input(page.code_input,answer)
    def page_login(self):
        self.base_click(page.click_dl)
    def page_withdrawing(self):
        # ele=self.base_click(page.click_withdrawing)

        # if not ele:
        #     return False
        # else:
        #     return True
        try:
            self.base_click(page.click_withdrawing)
            print("ture")
        except:
            print("false")











