Feature: Video playback and controls on Indeedemo FYC
  Background:
    Given I open the platform
    And I log in using the PIN

  Scenario: Automate video playback steps
    When I navigate to the Test Automation Project
    And I switch to the Details tab and wait
    And I return to the Videos tab
    And I play the video for 10 seconds then pause
    And I resume playback using Continue Watching
    And I set the volume to 50 percent
    And I change the resolution to 480p then back to 720p
    And I pause and go back
    Then I log out
