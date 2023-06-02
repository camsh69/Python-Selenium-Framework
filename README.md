# Python-Selenium-Framework

`cd` into tests folder to run tests - this ensures report.html, screenshots and logfiles are generated within tests folder

`pytest` to run all tests (default browser is Chrome),
`pytest --browser_name=firefox` to run test in a particular browser (also edge)
`pytest --html=report.html` to run test and generate a report.
Also `-v` for verbose, `-s` for added info and `-q` for quiet,

#### TO DO

Fix screenshotting

## Installs/Dependencies

### Download Python

https://www.python.org/downloads

Follow instructions of installer:

#### Windows

- Note the path where Python is being installed - generally C:\Users\(Your logged in User)\AppData\Local\Programs\Python\PythonXX

Set Python home in Environment Variables

- Do a search for 'Edit the system environment variables' in Windows
- Click on Environment Variables
- Edit 'Path'
- Set a new path to match the path where Python was installed
- Repeat above and add path for, e.g. C:\Users\(Your logged in User)\AppData\Local\Programs\Python\PythonXX/Scripts
- Open a new Command Prompt and enter: python --version
- If a response is returned then everything is installed fine

#### Mac

Path variable is automatically by MacOS on install

- Open a new terminal and enter: which python3
- If a response is returned with a path then everything is installed OK

## Install Selenium

https://pypi.org/project/selenium

(PIP is a python package manager - https://pip.pypa.io/en/stable/)

#### Windows

- In CMD
- `pip install selenium`
- To check: `pip show selenium`

#### Mac

- In a terminal
- `pip3 install selenium`
- To check: `pip3 show selenium`

\*\* Make sure the browsers on your machine, e.g. Chrome, are updated to latest version (Selenium will throw errors if it's version of, for example, Chromedriver doesn't match your version)

## Install PyTest

https://docs.pytest.org/en/7.1.x/getting-started.html

#### Windows

- `pip install -U pytest`

#### Mac

- `pip3 install -U pytest`

## Install Pytest-HTML

https://pypi.org/project/pytest-html

#### Windows

- `pip install -U pytest-html`

#### Mac

- `pip3 install -U pytest-htm`

## Install a code editor

VS Code - https://code.visualstudio.com/download

Pycharm - https://www.jetbrains.com/pycharm/download/ Free Community version
