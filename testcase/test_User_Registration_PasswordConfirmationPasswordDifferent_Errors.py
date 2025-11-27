import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：注册-密码和确认密码不一致
@pytest.mark.asyncio

@allure.story("注册-密码和确认密码不一致")
async def test_User_Registration_Success():
    async with async_playwright() as p:
        # 打开浏览器
        browser = await p.chromium.launch(headless=False,args=["--start-maximized"])
        try:
            page = await browser.new_page(no_viewport=True)
            #访问testsprite注册页面
            await page.goto("https://www.testsprite.com/auth/cognito/sign-up")
            await page.wait_for_timeout(3000)
            #输入账号email
            await page.fill('//*[@id=":r0:"]', "1@qq.com")
            await page.wait_for_timeout(3000)
            #输入密码
            await page.fill('//*[@id=":r1:"]', "12345678")
            await page.wait_for_timeout(3000)
            #输入确认密码
            await page.fill('//*[@id=":r2:"]', "123456789")
            await page.wait_for_timeout(3000)
            #点击Continue
            await page.click("text='Continue'")
            await page.wait_for_timeout(5000)
            #验证密码和确认密码不一致提示的文案
            loc=await page.locator('xpath=/html/body/div/div[1]/div/div/div/div[2]/form/div/div[3]/div[2]').inner_text()
            await page.wait_for_timeout(3000)
            assert loc=="Passwords don't match"
        finally:
            await browser.close()