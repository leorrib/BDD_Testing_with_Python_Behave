# E2E test on http://automationpractice.com
The following scenario is executed in this test:

- User visits aforementioned website, fills the search box with the name of the desired item and then proceeds to choose the item color and to checkout. 

## Requirements
- Python 3/pip (configure environment variables).
- Browser (chrome or firefox, although selenium local installation provides support for other browsers).
- An IDE.

## How to run the test
- Clone project.
- On the behave.ini file, indicate the desired browser (either chrome or firefox).
- Start a virtual environment on root level: 'pythom -m venv .venv'
- On root level, enter 'pip3 install -r requirements.txt' in order to install all necessary packages.
- In order to run the test without debugging, enter 'behave tests\features'
- In order to run the debug on error, enter 'behave -D debug=True tests\features'
- In order to run only tests marked by a specific tag, enter 'behave --tags="{tag name}" tests/features'
- In order to generate json reports, enter: 'behave -f json_allure -o reports tests/features'. 
- In order to read the above reports to html format, enter: 'allure serve reports/'. If allure is not configured in your path variables, make sure to install it globally (requires npm) by entering 'npm install -g allure-commandline --save-dev'
