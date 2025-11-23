import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：执行测试套件用例
@pytest.mark.asyncio
@allure.story("执行测试套件用例")

async def test_Dashboard_TESTING_TestLists_CreatList():
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
            #选择测试用例加入测试套件
            #点击Test Lists菜单
            await page.click("text='Test Lists'")
            await page.wait_for_timeout(3000)
            #点击某个Test List
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[1]/p")
            await page.wait_for_timeout(3000)
            #点击Run Test List
            await page.click("text='Run Test List'")
            await page.wait_for_timeout(8000)
            #验证列表中执行成功的状态
            loc=await page.locator('xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[5]/span').inner_text()
            await page.wait_for_timeout(3000)
            assert loc == 'Passed' or 'Failed'
        finally:
            await browser.close()
    