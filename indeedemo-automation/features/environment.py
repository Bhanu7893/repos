from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def before_all(context):
    
    
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # optional headless during development
    # options.add_argument('--headless')
    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.config.userdata['url'] = 'https://indeedemo-fyc.watch.indee.tv/'
    context.config.userdata['pin'] = 'WVMVHWBS'
    
    # Helper to dismiss cookie consent banner
    def dismiss_consent_banner(driver, wait):
        try:
            # Look for consent/cookie buttons and click accept or close
            accept_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'Accept All')]"))
            )
            accept_btn.click()
            time.sleep(0.5)
        except:
            try:
                close_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]")
                close_btn.click()
                time.sleep(0.5)
            except:
                pass
    
    # Store helper for use in steps
    context.dismiss_consent = dismiss_consent_banner
    context.wait = WebDriverWait(context.driver, 20)


def after_all(context):
    try:
        context.driver.quit()
    except Exception:
        pass
