import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：验证SETTINGS-API Keys新增功能
@pytest.mark.asyncio

@allure.story("验证SETTINGS-API Keys新增功能")
async def test_Dashboard_SETTINGS_APIKeys():
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
            #点击API Keys
            await page.click("text='API Keys'")
            await page.wait_for_timeout(5000)
            #删除数据
            await page.locator('[class="MuiIconButton-root MuiIconButton-variantPlain MuiIconButton-colorError.ghost MuiIconButton-sizeMd joy-ttwlcc"]').click()
            # 智能等待,等待页面加载完成
            await page.click("text='Revoke'")
            await page.wait_for_timeout(3000)
            # 验证SETTINGS-API Keys新增功能
            #点击New API Key按钮
            await page.click("text='New API Key'")
            await page.wait_for_timeout(3000)
            #输入Name
            await page.locator('[placeholder="Enter a name"]').fill('test1')
            await page.wait_for_timeout(3000)
            #点击Create按钮
            await page.click("text='Create'")
            await page.wait_for_timeout(3000)
            #点击Close按钮
            await page.click("text='Close'")
            await page.wait_for_timeout(3000)
            #新增成功，验证列表文案
            loc=await page.locator('text="test1"').inner_text()
            await page.wait_for_timeout(3000)
            assert loc == 'test1'
        finally:
            await browser.close()
    
