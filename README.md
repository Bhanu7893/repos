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

Notes
- Update Chrome or use chromedriver matching your Chrome version if needed.
- The demo video recording must be created locally by the user using screen recording tools; this repo includes optional code to record with OpenCV.
