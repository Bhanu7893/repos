# Run Behave tests with optional verbose output
param(
    [switch]$headless
)

if ($headless) {
    $env:BEHAVE_HEADLESS = '1'
}

# Activate venv if exists
if (Test-Path -Path ".\.venv\Scripts\Activate.ps1") {
    . .\.venv\Scripts\Activate.ps1
}

behave -f pretty
