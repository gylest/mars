# Evaluate Python

## Initial Setup

1. Install the Python extension for VS Code
2. Install a Python interpreter (version 3.13 installed on 27/09/2025)
3. Select Python Interpreter for VS Code (select latest version), from Command Palette enter "Python: Select Interpreter"

To show installed python versions on Windows enter this command in terminal window:-

```py -0```

## Package Management

The Python Package Index (PyPI) is a repository of software for the Python programming language.
The online library can be found here <https://pypi.org/>.
Use Package Installer for Python (pip) tool to install packages from this repository.  

Major packages used on this project:-

| Package    | Description |
|------------|-------------|
| beautifulsoup4 | Screen-scraping library |
| flask  | A simple framework for building complex web applications |
| lxml  | XML and HTML parser |
| numpy | Fundamental package for array computing with Python |
| pylint | python code static checker |
| pipdeptree | Command line utility to show dependency tree of packages |
| pyJWT | Python implementation of RFC 7519 (JSON Web Token) |
| python-dotenv | Read .env configuration file for python web applications |
| requests | Simplified HTTP library |
| selenium | Automate web browser interaction from Python |

Upgrade pip:-

`py -m pip install --upgrade pip`

List all installed packages in current Python enivironment:-

```py -m pip list```

Update outdated packages:-

`py -m pip list --outdated`

Update requirements.txt:-

`py -m pip freeze > requirements.txt`

Install project dependencies on a new machine:-

`py -m pip install -r requirements.txt`

## Linting using PyLint

Linting highlights syntactical and stylistic problems in your Python source code, which oftentimes helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors.

Linting should be enabled by default for PyLint, and errors are shown on Problems tab in terminal window.

PyLint's behavior is control through a .pylintrc configuration file.

For example to supress messages for "missing-function-docstring" add to section [MESSAGES CONTROL]

## Running a Script

1. Open PowerShell terminal window
2. Enter command:-

    ```py main.py```

## Debugging a Script

1. Open the script in editor
2. Set breakpoints in Python code
3. Select "Start Debugging" command or F5
4. Use debug toolbar to pause, continue, step over, step into, step out, restart and stop as required

## Testing using unittest

1. Enable a test framework using command "Python: Configure Tests". Select framework "unittest"
2. Set test file pattern "test*.py"
3. Open "Test" from the Activity Bar, and run command "Discover Tests" to fill Side bar with all tests found
4. Select command "Run All Tests" to run all the discovered tests
5. For any failed tests select from status bar then "View Test Output" to find details of error

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
