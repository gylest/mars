# Evaluate Python

## Initial Setup

1. Install the Python extension for VS Code  
2. Install a Python interpreter (version 3.14 installed on 08/10/2025)  
3. Select Python Interpreter for VS Code (select latest version), from Command Palette enter "Python: Select Interpreter"  
4. Select Python testing framework for VS Code (select PyTest), from command palette enter "Python: Configure Tests"  

To show installed python versions on Windows enter this command in terminal window:

```py -0```

## Python Standard Libary

The Python Standard Library is a collection of modules and packages included with every Python installation. These modules provide ready-to-use functionality for common programming tasks such as file I/O, system calls, networking, data manipulation, math operations, threading, and more without needing to install anything extra.

Some of the standard library modules used in this project:

| Module   | Description |
|------------|-------------|
| datetime | Date and time handling |
| json  | JSON parsing |
| math  | Mathmatical functions |
| os | Operating system interfaces |
| sys | System-specific parameters and functions |

## Package Management

The Python Package Index (PyPI) is a repository of software for the Python programming language.
The online store can be found here <https://pypi.org/>.  
Use Package Installer for Python (pip) tool to install packages from this repository.  

### Packages in Project

| Package    | Description |
|------------|-------------|
| beautifulsoup4 | Screen-scraping library |
| flask  | A simple framework for building complex web applications |
| lxml  | XML and HTML parser |
| numpy | Fundamental package for array computing with Python |
| pyJWT | Python implementation of RFC 7519 (JSON Web Token) |
| python-dotenv | Read .env configuration file for python web applications |
| requests | Simplified HTTP library |
| selenium | Automate web browser interaction from Python |

### Tools in Project

| Package    | Description |
|------------|-------------|
| coverage | Code coverage tool |
| debugpy | Debugger tool used by VSC |
| pipdeptree | Command line utility to show dependency tree of packages |
| pylint | Static code analyzer |
| pyTest | Python testing framework |

### pip Commands

Note: Prefix each pip command with "py -m" to ensure the current python environment.

|Description|Command|
|--|--|
|pip version|`python -m pip --version`|
|Upgrade pip|`python -m pip install --upgrade pip`|
|List packages in python environment|`python -m pip list`|
|List outdated packages|`python -m pip list --outdated`|
|Update requirements.txt|`python -m pip freeze > requirements.txt`|
|Install packages on new PC|`python -m pip install -r requirements.txt`|
|Install a package|`python -m pip install Flask`|
|Install specific version a package|`python -m pip install astroid==2.4.0`|
|Update package to latest version|`python -m pip install --upgrade pylint`|
|Uninstall a package|`python -m pip uninstall astroid`|
|Show information on a package|`python -m pip show Flask`|
|Verify packages|`python -m pip check`|
|Show package dependencies|`python -m pipdeptree`|

## Linting using PyLint

Linting highlights syntactical and stylistic problems in your Python source code, which oftentimes helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors.

Linting should be enabled by default for PyLint, and errors are shown on Problems tab in terminal window.

PyLint's behavior is control through a .pylintrc configuration file.

For example to supress messages for "missing-function-docstring" add to section [MESSAGES CONTROL]

## Running Scripts

1. Open PowerShell terminal window at root directory  
2. Run main : `python src/main.py`  
3. Run scrape_beautiful: `python src/scrape_beautifulsoop.py`  
4. Run todoservice: `python src/todoservice.py`  

## Debugging Scripts

1. Open the script in editor
2. Set breakpoints in Python code
3. Select "Start Debugging" command or F5
4. Use debug toolbar to pause, continue, step over, step into, step out, restart and stop as required

## Testing using PyTest

1. Open "Test" from the Activity Bar, and run command "Discover Tests" to fill Side bar with all tests found
2. Select command "Run All Tests" to run all the discovered tests
3. For any failed tests select from status bar then "View Test Output" to find details of error

## Code Coverage

1. Run tests with coverage: `coverage run -m pytest`  
2. Generate coverage report: `coverage report`  
3. Generate HTML report: `coverage html`  
4. Open file `htmlcov\index.html` with `Live Server`  

## Todo - Flask REST API Web Application

### Authentication using JWT

The REST API endpoints have JWT authentciation to make them more secure.  
THis means all methods except login require a valid bearer token.

Implementation steps:  

1. Add necessary librbaries to support JWT authentication:  
`pyJWT`, `Flask-Bcrypt`,`python-dotenv`  
2. Generate a JWT token on successful login with username and password  
3. Protect endpoints using decorator to validate JWT token  

### How to Run

1. Select debug launch configuration "Python: Flask"  
2. Press F5 to run and debug, or CTRL-F5 to run without debugging  
3. In Postman send Login POST request to get bearer token  
4. In the parent of the collection, open Auth tab, select Auth Type = `Bearer Token` and enter the bearer token value  
5. Execute the REST requests as needed i.e `Get Tasks` or `Post Task`  

## Improvements

1. In `todoservice.py` store valid users in a database and read at service launch.
