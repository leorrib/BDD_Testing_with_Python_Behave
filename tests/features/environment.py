from resources import DriverInit
from ipdb import spost_mortem

def before_all(context):
    context.browser = DriverInit(context)
    context.browser.implicitly_wait(15)
    context.browser.get(context.config.userdata.get('url'))

def after_step(context, step):
    if context.config.userdata.getbool('debug') and step.status == 'failed':
        spost_mortem(step.exc_traceback)

def after_all(context):
    context.browser.quit()