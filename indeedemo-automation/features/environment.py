from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


def before_all(context):
    options = Options()
    options.add_argument('--start-maximized')
    # optional headless during development
    # options.add_argument('--headless')
    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.config.userdata['url'] = 'https://indeedemo-fyc.watch.indee.tv/'
    context.config.userdata['pin'] = 'WVMVHWBS'


def after_all(context):
    try:
        context.driver.quit()
    except Exception:
        pass
