from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    PIN_INPUT = (By.CSS_SELECTOR, 'input[type="text"], input[type="password"], input[placeholder*="PIN"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button[type="submit"], button:contains("Enter")')

    def enter_pin_and_submit(self, pin):
        # try to find input
        pin_input = self.wait.until(EC.presence_of_element_located(self.PIN_INPUT))
        pin_input.clear()
        pin_input.send_keys(pin)
        # try submit
        try:
            btn = self.driver.find_element(*self.SUBMIT_BTN)
            btn.click()
        except Exception:
            pin_input.send_keys('\n')
