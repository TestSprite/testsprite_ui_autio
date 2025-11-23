import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：首页点击“Blog”跳转成功
@pytest.mark.asyncio

@allure.story("首页点击“Blog”跳转成功")
async def test_HomePage_redirect_Blog():
    async with async_playwright() as p:
        # 打开浏览器
        browser = await p.chromium.launch(headless=True,args=["--start-maximized"])
        try:
            page = await browser.new_page(no_viewport=True)
            #访问testsprite注册页面
            await page.goto("https://www.testsprite.com/",timeout=100000)
            # 通过xpath定位iframe
            # iframe = page.frame_locator("xpath=/html/body/div[1]/iframe")
            # 使用属性定位iframe
            iframe = page.frame_locator('iframe[src*="https://plucky-walkthroughs-714167.framer.app/"]')
            await page.wait_for_timeout(3000)
            # 点击Blog
            await iframe.locator('text="Blog"').click()
            await page.wait_for_timeout(3000)
            # 获取文案
            loc =await iframe.locator('text="Compiled notes from the TestSprite team"').inner_text()
            assert loc == "Compiled notes from the TestSprite team"
        finally:
            await browser.close()