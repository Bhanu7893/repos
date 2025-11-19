Indeedemo FYC Automation

This project automates video playback tasks on the Indeedemo FYC platform using Python, Selenium and Behave (BDD).

Setup

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the tests (Behave):

```powershell
behave
```

Structure
- features/: Behave feature files
- features/steps/: Step implementations
- pages/: Page Object Model classes
- env.py: Behave environment and driver setup

Usage

You can override the default URL and PIN when running behave:

```powershell
behave -D url=https://indeedemo-fyc.watch.indee.tv/ -D pin=WVMVHWBS
```

Run the provided PowerShell helper:

```powershell
.\run_tests.ps1
```

Record a demo using any screen recorder (e.g., OBS, Windows Game Bar). The code includes an optional `utils/recorder.py` as a placeholder for programmatic recording.

Notes
- Update Chrome or use chromedriver matching your Chrome version if needed.
- The demo video recording must be created locally by the user using screen recording tools; this repo includes optional code to record with OpenCV.

# End
