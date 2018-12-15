import sys
import os

from base.read_yaml import ReadLogin

sys.path.append(os.getcwd())

def get_data():
    datas = ReadLogin("data_login.yaml").read_ts()
    arrs=[]
    for data in datas.values():
        arrs.append((data.get("username"),data.get("pwd")))
    return arrs



import pytest
from page.page_login import Pagelogin
from base.get_driver import get_driver
'''
        实例化页面
        点击登录模块
        输入用户名
        输入密码
        输入验证码
        点击登录
        验证是否成功
        关闭页面
        
        '''
class TestLogin():
    def setup_class(self):
        print("set_up")
        self.login=Pagelogin(get_driver())
    def teardown_class(self):
        print("teardown")
        self.login.driver.quit()
    @pytest.mark.parametrize("username,pwd",get_data())
    def test_login(self,username,pwd):
        self.login.page_register()
        self.login.page_username(username)
        self.login.page_password(pwd)
        self.login.page_code()
        self.login.page_login()
        self.login.page_withdrawing()
        # self.login.page_register()


if __name__ == '__main__':
    print(get_data())
    pytest.main()