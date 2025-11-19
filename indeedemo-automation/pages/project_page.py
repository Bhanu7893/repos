import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProjectPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators (may need adjustments)
    ALL_TITLES = (By.XPATH, "//a[contains(., 'All Titles') or contains(., 'All titles')]")
    TEST_PROJECT = (By.XPATH, "//div[contains(., 'Test Automation Project') or contains(., 'Test automation project')]")
    DETAILS_TAB = (By.XPATH, "//button[contains(., 'Details')]")
    VIDEOS_TAB = (By.XPATH, "//button[contains(., 'Videos')]")
    FIRST_VIDEO_PLAY = (By.CSS_SELECTOR, 'button.play, .video-play, video')
    CONTINUE_WATCHING = (By.XPATH, "//button[contains(., 'Continue Watching')]")
    VOLUME_HANDLE = (By.CSS_SELECTOR, '.volume input[type=range], .vjs-volume-bar')
    SETTINGS_BTN = (By.CSS_SELECTOR, '.settings-button, .vjs-settings-button')
    RESOLUTION_MENU = (By.XPATH, "//div[contains(@class,'quality') or contains(., '480p')]")
    BACK_BTN = (By.CSS_SELECTOR, 'button.back, .back-button')
    LOGOUT_BTN = (By.XPATH, "//button[contains(., 'Logout') or contains(., 'Sign out')]")

    def open_test_automation_project(self):
        # Optionally click All Titles then the project
        try:
            self.wait.until(EC.element_to_be_clickable(self.ALL_TITLES)).click()
        except Exception:
            pass
        self.wait.until(EC.element_to_be_clickable(self.TEST_PROJECT)).click()

    def click_details_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.DETAILS_TAB)).click()

    def click_videos_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.VIDEOS_TAB)).click()

    def play_first_video(self):
        # attempt clicking a play button or the video element
        el = self.wait.until(EC.element_to_be_clickable(self.FIRST_VIDEO_PLAY))
        try:
            el.click()
        except Exception:
            # fallback: use JS to play video
            self.driver.execute_script("document.querySelector('video').play();")

    def pause_video(self):
        try:
            self.driver.execute_script("document.querySelector('video').pause();")
        except Exception:
            pass

    def click_continue_watching(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CONTINUE_WATCHING)).click()
        except Exception:
            # fallback: click on video to resume
            try:
                self.driver.execute_script("document.querySelector('video').play();")
            except Exception:
                pass

    def set_volume(self, fraction: float):
        # set via JS to be robust
        vol = max(0.0, min(1.0, float(fraction)))
        self.driver.execute_script(f"document.querySelector('video').volume = {vol};")

    def change_resolution(self, res_label: str):
        # open settings and choose resolution text
        try:
            self.wait.until(EC.element_to_be_clickable(self.SETTINGS_BTN)).click()
            # wait for menu and click resolution
            menu = self.wait.until(EC.presence_of_element_located(self.RESOLUTION_MENU))
            # choose link by text
            item = menu.find_element(By.XPATH, ".//button[contains(., '%s') or contains(., '%s') or contains(., '%s') ]" % (res_label, res_label.replace('p',''), res_label))
            item.click()
        except Exception:
            # fallback: use player API if present
            try:
                if 'player' in self.driver.execute_script('return window'):
                    self.driver.execute_script("window.player.setQuality('%s')" % res_label)
            except Exception:
                pass

    def wait_seconds(self, s):
        time.sleep(s)

    def click_back(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.BACK_BTN)).click()
        except Exception:
            self.driver.back()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()
