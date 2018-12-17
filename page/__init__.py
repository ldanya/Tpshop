from selenium.webdriver.common.by import By

# 点击登录
click_login=By.XPATH,"//*[contains(@class,'red')]"
username_input=By.ID,"username"
password_input=By.ID,"password"
code_input=By.ID,"verify_code"
click_dl=By.CLASS_NAME,"J-login-submit"
click_withdrawing=By.XPATH,"//*[contains(text(),'退出')]"
