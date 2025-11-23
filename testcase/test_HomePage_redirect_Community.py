import asyncio

import allure
import pytest
from playwright.async_api import expect, async_playwright

#用例名称：首页点击“Community”跳转成功
@pytest.mark.asyncio

@allure.story("首页点击“Community”跳转成功")
async def test_HomePage_redirect_Community():
    async with async_playwright() as p:
        # 打开浏览器
        browser = await p.chromium.launch(headless=False,args=["--start-maximized"])
        try:
            page = await browser.new_page(no_viewport=True)
            #访问testsprite注册页面
            await page.goto("https://www.testsprite.com/",timeout=100000)
            # 使用属性定位iframe
            iframe = page.frame_locator('iframe[src*="https://plucky-walkthroughs-714167.framer.app/"]')
            await page.wait_for_timeout(3000)
            # 点击Community
            await iframe.locator('text="Community"').click()
            await page.wait_for_timeout(100000)
            # 获取所有窗口
            all_pages = browser.contexts[0].pages
            # 在窗口间切换操作
            for i, page in enumerate(all_pages):
                # 切换窗口 通过下标切换窗口 0 代表初始窗口 1代表新打开的窗口
                if i==1:
                    #获取文案
                    loc = await iframe.locator('xpath=/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div[2]/div[3]/button/div/div/span').inner_text()
                    assert loc=="创建账户"
        finally:
            await browser.close()