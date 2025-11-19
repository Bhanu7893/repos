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
    DETAILS_TAB = (By.XPATH, "//a[@id='detailsSection']")
    VIDEOS_TAB = (By.XPATH, "//a[@id='videosSection']")
    FIRST_VIDEO_PLAY = (By.XPATH, "(//button[@aria-label='Play Video'])[1]")
    PAUSE_VIDEO_PLAY = (By.XPATH, "(//div[@aria-label='Pause'])[2]")   
    CONTINUE_WATCHING = (By.XPATH, "//button[contains(., 'Continue Watching')]")
    VOLUME_HANDLE = (By.CSS_SELECTOR, '.volume input[type=range], .vjs-volume-bar')
    SETTINGS_BTN = (By.XPATH, "(//div[@aria-label='Settings'])[2]")
    RESOLUTION_480P = (By.XPATH, "//button[@aria-label='480p']")
    RESOLUTION_720P = (By.XPATH, "//button[@aria-label='720p']")
    RESOLUTION_MENU = (By.XPATH, "//div[contains(@class,'quality') or contains(., '480p')]")
    BACK_BTN = (By.CSS_SELECTOR, 'button.back, .back-button')
    LOGOUT_BTN = (By.XPATH, "//button[@id='signOutSideBar']")

    def open_test_automation_project(self):
        # Find and click on the Test Automation Project tile/card
        import time
        try:
            # Try different selectors for project tile
            elem = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Test automation project']")))
            # Scroll to element using JavaScript
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elem)
            time.sleep(1)
            # Click using JavaScript if regular click fails
            try:
                elem.click()
            except:
                self.driver.execute_script("arguments[0].click();", elem)
            time.sleep(10)
        except Exception as e:
            print(f"Error opening project: {e}")
            raise

    def click_details_tab(self):
        import time
        elem = self.wait.until(EC.presence_of_element_located(self.DETAILS_TAB))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        time.sleep(0.5)
        try:
            elem.click()
        except:
            self.driver.execute_script("arguments[0].click();", elem)

    def click_videos_tab(self):
        import time
        elem = self.wait.until(EC.presence_of_element_located(self.VIDEOS_TAB))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        time.sleep(0.5)
        try:
            elem.click()
        except:
            self.driver.execute_script("arguments[0].click();", elem)

    def play_first_video(self):
        import time
        # Try multiple strategies to play the video
    
            # Strategy 1: Find and click play button
        play_btn = self.wait.until(EC.presence_of_element_located(self.FIRST_VIDEO_PLAY))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", play_btn)
        time.sleep(0.5)
        try:
            play_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", play_btn)
        time.sleep(1)

    def pause_video(self):
        import time
        try:
            # Try to pause via iframe
            iframe = self.driver.find_element(By.ID, "video_player")
            self.driver.switch_to.frame(iframe)
            
            # Click on the video player area to pause
            app_elem = self.driver.find_element(By.ID, "app")
            app_elem.click()
            time.sleep(0.5)
            
            self.driver.switch_to.default_content()
        except:
            # Fallback: pause via JavaScript on main video element
            try:
                self.driver.execute_script("document.querySelector('video').pause();")
            except:
                pass
        
        time.sleep(1)

    def click_continue_watching(self):
        import time
        try:
            # Try to pause via iframe
            iframe = self.driver.find_element(By.ID, "video_player")
            self.driver.switch_to.frame(iframe)
            
            # Click on the video player area to pause
            app_elem = self.driver.find_element(By.ID, "app")
            app_elem.click()
            time.sleep(0.5)
            
            self.driver.switch_to.default_content()
        except:
            # Fallback: pause via JavaScript on main video element
            try:
                self.driver.execute_script("document.querySelector('video').play();")
            except:
                pass
        
        time.sleep(1)

    def set_volume(self, fraction: float):
        import time
        # set via JS to be robust
        vol = max(0.0, min(1.0, float(fraction)))
        
        try:
            # Try to set volume via iframe
            iframe = self.driver.find_element(By.ID, "video_player")
            self.driver.switch_to.frame(iframe)
            
            self.driver.execute_script(f"document.querySelector('video').volume = {vol};")
            
            self.driver.switch_to.default_content()
        except:
            # Fallback: try to set volume on main page
            try:
                self.driver.execute_script(f"document.querySelector('video').volume = {vol};")
            except:
                pass
        
        time.sleep(0.5)

    def change_resolution(self, res_label: str):
        import time
        # open settings and choose resolution text
        try:
            # Try to change resolution via iframe
            iframe = self.driver.find_element(By.ID, "video_player")
            self.driver.switch_to.frame(iframe)
            
            settings_btn = self.wait.until(EC.element_to_be_clickable(self.SETTINGS_BTN))
            settings_btn.click()
            time.sleep(0.5)
            
            # wait for menu and click resolution
            res_480p= self.wait.until(EC.presence_of_element_located(self.RESOLUTION_480P))
            # choose link by text
            
            res_480p.click()
            time.sleep(0.5)
            res_720p= self.wait.until(EC.presence_of_element_located(self.RESOLUTION_720P))
            # choose link by text
            
            res_720p.click()
            
            self.driver.switch_to.default_content()
            return
        except:
            self.driver.switch_to.default_content()
        
        
    def wait_seconds(self, s):
        time.sleep(s)

    def click_back(self):
        import time
        try:
            elem = self.wait.until(EC.presence_of_element_located(self.BACK_BTN))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            time.sleep(0.5)
            try:
                elem.click()
            except:
                self.driver.execute_script("arguments[0].click();", elem)
        except Exception:
            # Fallback to browser back
            self.driver.back()

    def logout(self):
        import time
        elem = self.wait.until(EC.presence_of_element_located(self.LOGOUT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        time.sleep(0.5)
        try:
            elem.click()
        except:
            self.driver.execute_script("arguments[0].click();", elem)
