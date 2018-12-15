import os

import yaml

class ReadLogin():
    def __init__(self,findname):
       self.findname=os.getcwd()+os.sep+"data"+os.sep+findname
    # 打开文件
    def read_login(self):
        with open(self.findname,"r",encoding="utf-8") as f:
            print(yaml.load(f))

    # 以下方法 为右键调试使用
    def read_ts(self):
        with open("./data/data_login.yaml","r",encoding="utf-8") as f:
            return  yaml.load(f)

if __name__ == '__main__':

        datas=ReadLogin("data_login.yaml").read_ts()

