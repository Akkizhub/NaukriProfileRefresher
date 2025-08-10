# Daily Naukri Update
[![license](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/navchandar/Naukri/blob/master/LICENSE) 
[![Test](https://github.com/navchandar/Naukri/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/navchandar/Naukri/actions/workflows/main.yml)
[![Code Climate](https://codeclimate.com/github/navchandar/Naukri.svg)](https://codeclimate.com/github/navchandar/Naukri)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 


### Selenium and Python powered automation script

This script automates information updates on the job portal "Naukri". Most recruiters may filter users with the most recent updates on their profile.

Use this script to update your Naukri Profile on schedule every day; this can be completed in seconds.

In order to use this, you need Git, Python 3, and Google Chrome on your machine.


## Installation

Install [Python 3.10+](https://www.python.org/getit/) and run the below commands

```bash
git clone https://github.com/navchandar/Naukri.git
cd Naukri
pip install --upgrade pip
python3 -m venv .venv              # create virtual environment for installing dependencies
./.venv/bin/activate.ps1           # source ./.venv/bin/activate  # command for macOS/linux
pip install -r requirements.txt    # Install dependencies
```

Configuration: Update `RESUME_PATH`, `USERNAME`, `PASSWORD`, and `MOBILE` directly in `constants.py` before running the script.

### Run the Script
```bash
python naukri.py
```


## Browsers support

| [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" alt="Chrome" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br>Chrome |
| --------- |
| last 10 versions


## Contribute

Contributions are always welcome!

Please read the [contribution guidelines](contributing.md) first.

## Disclaimer

This script is not affiliated with or endorsed by Naukri.com.

It is intended for personal use to help improve profile visibility, but results are not guaranteed. Effectiveness may vary based on recruiter behavior and platform factors.

Ensure compliance with Naukri.com’s terms of service. The script does not store or share personal data. Use responsibly and at your own risk.


## Reference Links

[Python 3+](https://www.python.org/downloads/)

[Selenium 3+](http://seleniumhq.org/download/)

[Google Chrome](https://www.google.com/intl/en/chrome/browser/desktop/index.html?standalone=1)

[Chrome Driver](https://chromedriver.chromium.org/downloads)

[How to Use Task Scheduler](https://www.wikihow.com/Use-Task-Scheduler-(in-Vista))

