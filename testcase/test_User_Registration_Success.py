import asyncio
import random

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：注册成功
@pytest.mark.asyncio

@allure.story("注册成功")
async def test_User_Registration_Success():
    async with async_playwright() as p:
        # 打开浏览器
        browser = await p.chromium.launch(headless=False,args=["--start-maximized"])
        try:
            page = await browser.new_page(no_viewport=True)
            #访问testsprite注册页面
            await page.goto("https://www.testsprite.com/auth/cognito/sign-up")
            await page.wait_for_timeout(3000)
            #随机邮箱
            mail=str(random.randint(20, 100000))+"@qq.com"
            #输入账号email
            await page.fill('//*[@id=":r0:"]',mail)
            await page.wait_for_timeout(3000)
            #输入密码
            await page.fill('//*[@id=":r1:"]', "Cs123456.")
            await page.wait_for_timeout(3000)
            #输入确认密码
            await page.fill('//*[@id=":r2:"]', "Cs123456.")
            await page.wait_for_timeout(3000)
            #点击Continue
            await page.click("text='Continue'")
            await page.wait_for_timeout(8000)
            #验证注册成功后跳转的页面的文案
            loc=await page.locator('xpath=/html/body/div[1]/div[1]/div/div/div/span[1]').inner_text()
            print(loc)
            await page.wait_for_timeout(3000)
            assert loc=='Confirm Your Email'
        finally:
            await browser.close()