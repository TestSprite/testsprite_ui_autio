import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：首页访问成功
@pytest.mark.asyncio

@allure.story("首页访问成功")
async def test_HomePage_info():
    async with async_playwright() as p:
        # 打开浏览器
        browser = await p.chromium.launch(headless=True,args=["--start-maximized"])
        try:
            page = await browser.new_page(no_viewport=True)
            #访问testsprite注册页面
            await page.goto("https://www.testsprite.com/",timeout=100000)
            #验证首页的文案
            # 通过xpath定位iframe
            # iframe = page.frame_locator("xpath=/html/body/div[1]/iframe")
            # 使用属性定位iframe
            iframe = page.frame_locator('iframe[src*="https://plucky-walkthroughs-714167.framer.app/"]')
            await asyncio.sleep(3)
            # 在iframe内部定位元素
            # loc=await iframe.locator('xpath=//*[@id="undefined-1w55ync"]/a/div/p').inner_text()
            loc = await iframe.locator('text="Solutions"').inner_text()
            await page.wait_for_timeout(3000)
            assert loc=="Solutions"
        finally:
            await browser.close()