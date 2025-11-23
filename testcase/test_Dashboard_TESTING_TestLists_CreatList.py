import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：新建测试套件
@pytest.mark.asyncio

@allure.story("新建测试套件")
async def test_Dashboard_TESTING_TestLists():
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
            #删除原先的JustForTest
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[6]/button")
            await page.wait_for_timeout(3000)
            #点击“Delete Test List”按钮
            await page.click("text='Delete Test List'")
            await page.wait_for_timeout(3000)
            #点击Delete按钮
            await page.click("text='Delete'")
            await page.wait_for_timeout(3000)
            #点击“New List”
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/button")
            await page.wait_for_timeout(3000)
            #输入Test Lists名称
            await page.fill("xpath=/html/body/div[3]/div[3]/div/div[1]/div/div/input",'JustForTest')
            await page.wait_for_timeout(3000)
            #点击Add
            await page.click("text='Add'")
            await page.wait_for_timeout(3000)
            #验证列表中新增成功的Test Lists
            loc=await page.locator('xpath=/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[1]/p').inner_text()
            await page.wait_for_timeout(3000)
            assert loc == 'JustForTest'
        finally:
            # 点击JustForTest
            await page.click("text='JustForTest'")
            await page.wait_for_timeout(3000)
            # 点击Add Tests
            await page.click("text='Add Tests'")
            await page.wait_for_timeout(3000)
            # 通过Creation Name筛选测试用例
            await page.fill("xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/input", 'test1')
            await page.wait_for_timeout(3000)
            # 点击选择第一个
            await page.click("xpath=/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[1]/span/span/span/input")
            await page.wait_for_timeout(3000)
            # 点击Add to Test List
            await page.click("text='Add to Test List'")
            await page.wait_for_timeout(3000)
            await browser.close()
    