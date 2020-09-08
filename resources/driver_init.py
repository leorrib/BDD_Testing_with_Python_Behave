from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox, FirefoxOptions

def DriverInit(context):
    browser = context.config.userdata.get('browser')
    browsers = {
        'chrome': [Chrome, ChromeOptions],
        'firefox': [Firefox, FirefoxOptions]
    }   
    opts = browsers[browser][1]()
    opts.add_argument("user-agent=mrbean")
    opts.add_argument("--start-maximized")
    context.browser = browsers[browser][0](options = opts)
    return context.browser