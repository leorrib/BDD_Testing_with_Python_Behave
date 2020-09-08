from behave import given, when, then
from tests.page_objects import *

@given(u'the user searches for "{item}" at the homepage')
def searches_for_desired_item(context, item):
    lp = LandingPage(context.browser)
    lp.search_for_item(item)
    

@when(u'picks the color "{color_spec}" for the "{item}" and adds the item to the cart')
def picks_the_collor(context, color_spec, item):
    srp = SearchResultPage(context.browser)
    ip = ItemPage(context.browser)

    srp.check_result_and_click_item(item)
    ip.check_name_and_pick_a_color(item, color_spec)
    ip.add_to_cart_and_checkout()
    

@then(u'verifies that "{quantity}" item "{item}", with price "{value}" and color "{desired_color}", was added to the cart and checks the final price')
def validates_the_result(context, quantity, item, value, desired_color):
    cp = CheckoutPage(context.browser)
    cp.validate_result(item, desired_color, value, quantity)

@then(u'verifies that the item is not available and that the message "{message}" is displayed')
def step_impl(context, message):
    srp = SearchResultPage(context.browser)
    srp.validate_alert(message)