# -*- coding: utf-8 -*-
# @Author  :zr
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import pytest
# -*- coding: utf-8 -*-
# @Author  :zr
# -*- coding: utf-8 -*-
# @Author  :zr
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()


# 登录获取客户列表()
def test_loginAndInitialize ():
    """
    登录和初始化
    """
    # 获取driver
    # 打开连接
    driver.get("https://background-test.uofferglobal.com/#/login?redirect=%2Fdashboard")
    # 窗口最大化
    driver.maximize_window()
    # 输入账号
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')).send_keys("zr")
    # 输入密码
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input')).send_keys("123456")
    # 点击登录
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/form/button')).click()
    time.sleep(3)
    # 点击财务报表
    try:
        # 点击财务报表
        WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,
                                                                 '//*[@id="app"]/div/div   [1]/div[2]/div[1]/div/ul/div[7]/li/div')).click()
        time.sleep(2)
    except Exception as e:
        # 点击三横杠
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.XPATH, ' // *[ @ id = "app"] / div / div[1] / div[1] / div / div')).click()
        time.sleep(2)
        # 点击财务报表
        WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,
                                                                 '//*[@id="app"]/div/div   [1]/div[2]/div[1]/div/ul/div[7]/li/div')).click()
        time.sleep(2)
    # 点击收款管理
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,
                                                             '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[1]/a/li/span')).click()
    return driver




# 断言一个列表中的元素包含另一个元素
#var 中的元素包含 srk
def assertInAndprint(var, tip, srk):
    try:
        # 遍历列表标签获取到标签对应的文本值保存到text
        texts = [i.text for i in var]
        # 对获取到的列表值输出
        print(texts)
        # 断言判断输入框的内容是否在列表中
        for i in texts:
            if srk in i:
                # 如果在不执行任何语句
                pass
            else:
                # 如果不存在返回查询功能未实现
                return tip + "未实现"
        return tip + "已实现"
    except Exception as e:
        return e


# 断言一个列表中的元素等于另一个元素
def assertequalAndprint(var, tip, srk):
    try:
        # 遍历列表标签获取到标签对应的文本值保存到text李
        texts = [i.text for i in var]
        # 对获取到的列表值输出
        print(texts)
        # 断言判断输入框的内容是否在列表中
        for i in texts:
            if srk == i:
                # 如果在不执行任何语句
                pass
            else:
                # 如果不存在返回查询功能未实现
                return tip + "未实现"
        return tip + "已实现"
    except Exception as e:
        return e

# 断言一个时间是否在两个时间段之间
def assertTimeAndprint(start_time, end_time, listtime, tip):
    try:
        start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d")
        end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d")
        # 遍历列表标签获取到标签对应的文本值保存到text李
        texts = [i.text for i in listtime]
        # 对获取到的列表值输出
        print(texts)
        # 断言判断输入框的内容是否在列表中
        for i in texts:

            check_time = datetime.datetime.strptime(i, "%Y-%m-%d")
            if start_time <= check_time <= end_time:
                # 如果在不执行任何语句
                pass
            else:
                # 如果不存在返回查询功能未实现
                return tip + "未实现"
        return tip + "已实现"
    except Exception as e:
        return e
#断言 两个个元素的关系是否相等或者包含
def assertInOrEqualAndprint(var, tip, srk,equalOrIn):
    if(equalOrIn=="equal"):
        if(var==srk):
            return tip+"已实现"
        else:
            return tip+ "未实现"
    elif (equalOrIn == "in"):
        if srk in var:
            return tip + "已实现"
        else:
            return tip + "未实现"
    else:
        return tip+"传入的判断方式有误"




