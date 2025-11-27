import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：登录成功
@pytest.mark.asyncio

@allure.story("登录成功")
async def test_User_Login_Success():
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
            await page.wait_for_timeout(3000)
            #验证登录成功后跳转的页面的文案
            loc=await page.locator('xpath=/html/body/div[1]/div[1]/div/div[1]/div[1]/div/a[1]/span[2]').inner_text()
            await page.wait_for_timeout(3000)
            assert loc == 'Home'
        finally:
            await browser.close()
    