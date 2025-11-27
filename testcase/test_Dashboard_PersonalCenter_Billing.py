import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：个人中心-点击Billing跳转成功
@pytest.mark.asyncio

@allure.story("个人中心-点击Billing跳转成功")
async def test_Dashboard_PersonalCenter_Billing():
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
            #验证个人中心-点击Billing跳转成功
            #点击头像
            await page.click("xpath=/html/body/div[1]/div[2]/div[1]/div[2]/button/div")
            await page.wait_for_timeout(3000)
            # 点击Billing
            await page.click("xpath=/html/body/ul/a[2]")
            await page.wait_for_timeout(3000)
            #跳转成功，验证跳转后页面文案
            # 跳转成功，验证跳转后页面文案
            loc = await page.locator(
                'xpath=/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/span').inner_text()
            await page.wait_for_timeout(3000)
            assert loc == '1st-Month Discount'
        finally:
            await browser.close()
    
