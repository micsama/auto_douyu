from playwright.sync_api import sync_playwright
from time import sleep
def getCookie():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge",headless=False)
        page = browser.new_page()
        page.goto("https://douyu.com")
        page.click("//html/body/div[1]/header/div/div/div/div[3]/div[8]/div/div/a/span")
        sleep(20)
        storage = page.context.storage_state(path="state.json")
        print(storage)
        browser.close()
def ygb():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state="state.json")
        page=context.new_page()
        page.goto("https://www.douyu.com/957090")
        i_path="//html/body/section/main/div[5]/div[1]/div[5]/div/div[2]/div/div[2]/div/div[5]/div/div/div/div[2]/div[2]/div/div[1]/ul[1]/li[1]/span"
        anniu_path="//html/body/section/main/div[5]/div[1]/div[5]/div/div[2]/div/div[2]/div/div[5]/div/div/div/div[2]/div[2]/div/div[1]/ul[1]/li[1]/img"
        x_path="//html/body/section/main/div[5]/div[1]/div[4]/div[1]/div[1]/div[9]/div[1]"
        x2_path="//html/body/div[18]/div[1]"
        beibao_path="//html/body/section/main/div[5]/div[1]/div[5]/div/div[2]/div/div[2]/div/div[5]/div/div/span"
        page.click(x_path)#关掉广告
        page.click(x2_path)#关掉广告
        page.click(beibao_path)
        i=page.inner_text(i_path)
        for j in range(i):
            page.click(anniu_path)
            page.wait_for_timeout(500)
        print(i)
def fun1():
    while(1):
        sleep(24*60*60)
        ygb()
    pass
if __name__ == "__main__":
    ygb()
    # getCookie()
