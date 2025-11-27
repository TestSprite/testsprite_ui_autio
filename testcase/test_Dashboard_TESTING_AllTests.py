import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：选择测试用例加入测试套件
@pytest.mark.asyncio

@allure.story("选择测试用例加入测试套件")
async def test_Dashboard_TESTING_AllTests():
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
            #点击All Tests菜单
            await page.click("text='All Tests'")
            await page.wait_for_timeout(3000)
            #通过Creation Name筛选测试用例
            await page.fill("xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/input",'test1')
            await page.wait_for_timeout(3000)
            #选择测试用例
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[1]/span/span/span/input")
            await page.wait_for_timeout(3000)
            #点击Add to Test List
            await page.click("text='Add to Test List'")
            await page.wait_for_timeout(3000)
            #选择Test List
            await page.click('text="JustForTest"')
            await page.wait_for_timeout(3000)
            #点击Add
            await page.click("text='Add'")
            await page.wait_for_timeout(4000)
            #验证页面文案
            loc=await page.locator('xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/span').inner_text()
            loc1 = await page.locator(
                'xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div/table/tbody/tr/td[3]/button').inner_text()
            await page.wait_for_timeout(3000)
            assert loc == 'JustForTest' and loc1=='test1'
        finally:
            await browser.close()
    