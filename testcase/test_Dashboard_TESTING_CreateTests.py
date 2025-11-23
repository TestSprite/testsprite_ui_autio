import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：创建测试成功
@pytest.mark.asyncio

@allure.story("创建测试成功")
async def test_Dashboard_TESTING_CreateTests():
    async with async_playwright() as p:
        # 打开浏览器
        browser = await p.chromium.launch(headless=False,args=["--start-maximized"])
        try:
            page = await browser.new_page(no_viewport=True)
            #访问testsprite登录页面
            await page.goto("https://www.testsprite.com/auth/cognito/sign-in")
            # 输入账号
            await page.fill('//*[@id=":r0:"]', "15213337472@163.com")
            await page.wait_for_timeout(3000)
            # 输入密码
            await page.fill('//*[@id=":r1:"]', "Cs123456.")
            await page.wait_for_timeout(3000)
            #点击登录
            await page.click("text='Continue'")
            await page.wait_for_timeout(5000)
            #清除之前的数据
            # 点击All Tests菜单
            await page.click("text='All Tests'")
            await page.wait_for_timeout(3000)
            # 通过Creation Name筛选测试用例
            await page.fill("xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/input", 'test1')
            await page.wait_for_timeout(3000)
            # 点击后面的按钮
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[5]/button")
            await page.wait_for_timeout(3000)
            # 点击"Delete"按钮
            await page.click("text='Delete'")
            await page.wait_for_timeout(3000)
            #验证创建测试成功
            #点击Create Tests菜单
            await page.click("text='Create Tests'")
            await page.wait_for_timeout(3000)
            # 输入Test Name
            await page.fill("xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div/div[2]/div/input",'test1')
            await page.wait_for_timeout(3000)
            #点击Next按钮
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div/div[4]/button")
            await page.wait_for_timeout(3000)
            #输入API name
            await page.fill('xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div[1]/div[1]/div/div/input', "login1")
            await page.wait_for_timeout(3000)
            #输入API endpoint/URL
            await page.fill('xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div[1]/div[2]/div/div/input', "https://background-live.uofferglobal.com/backend/api/v1/User/login")
            await page.wait_for_timeout(3000)
            #选择Authentication Type
            await page.locator('xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div[1]/div[3]/div/button/div').click()
            await page.wait_for_timeout(3000)
            #选择Bearer
            await page.locator('xpath=/html/body/ul/li[1]/div').click()
            await page.wait_for_timeout(3000)
            #输入Extra testing information
            await page.fill('xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div[1]/div[5]/div/textarea[1]', '{"user_name":"11111@qq.com","password":"cs123456"}')
            await page.wait_for_timeout(3000)
            # 点击Next按钮
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div[3]/div/button[3]")
            await page.wait_for_timeout(3000)
            # 再次点击Next按钮
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/button[2]")
            await page.wait_for_timeout(3000)
            #点击取消所有
            await page.click('xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/span/span/span/input')
            await page.wait_for_timeout(3000)
            #选择第一个
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/span/span/span/input")
            await page.wait_for_timeout(3000)
            # 再次点击Next按钮
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/button[2]")
            await page.wait_for_timeout(3000)
            #新建成功，验证页面文案
            loc=await page.locator('xpath=/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/span[1]').inner_text()
            await page.wait_for_timeout(3000)
            assert loc == 'Passed' or 'Failed'
        finally:
            await browser.close()
    