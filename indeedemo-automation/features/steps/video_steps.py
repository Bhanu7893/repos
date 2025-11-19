from behave import given, when, then
from pages.login_page import LoginPage
from pages.project_page import ProjectPage

@given('I open the platform')
def step_open_platform(context):
    context.driver.get(context.config.userdata.get('url', 'https://indeedemo-fyc.watch.indee.tv/'))

@given('I log in using the PIN')
def step_login(context):
    login = LoginPage(context.driver)
    pin = context.config.userdata.get('pin', 'WVMVHWBS')
    login.enter_pin_and_submit(pin)

@when('I navigate to the Test Automation Project')
def step_navigate_project(context):
    proj = ProjectPage(context.driver)
    proj.open_test_automation_project()

@when('I switch to the Details tab and wait')
def step_details_tab(context):
    proj = ProjectPage(context.driver)
    proj.click_details_tab()
    proj.wait_seconds(6)

@when('I return to the Videos tab')
def step_videos_tab(context):
    proj = ProjectPage(context.driver)
    proj.click_videos_tab()

@when('I play the video for 10 seconds then pause')
def step_play_pause(context):
    proj = ProjectPage(context.driver)
    proj.play_first_video()
    proj.wait_seconds(10)
    proj.pause_video()

@when("I resume playback using Continue Watching")
def step_continue_watching(context):
    proj = ProjectPage(context.driver)
    proj.click_continue_watching()

@when('I set the volume to 50 percent')
def step_set_volume(context):
    proj = ProjectPage(context.driver)
    proj.set_volume(0.5)

@when('I change the resolution to 480p then back to 720p')
def step_change_resolution(context):
    proj = ProjectPage(context.driver)
    proj.change_resolution('480p')
    proj.wait_seconds(2)
    proj.change_resolution('720p')

@when('I pause and go back')
def step_pause_and_back(context):
    proj = ProjectPage(context.driver)
    proj.pause_video()
    proj.click_back()

@then('I log out')
def step_logout(context):
    proj = ProjectPage(context.driver)
    proj.logout()
