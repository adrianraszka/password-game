import pytest
import random
import re
from password_generator import PasswordGenerator
from password_page_locators import PasswordPage
from password_rules import rules
from playwright.sync_api import Page, expect

pg = PasswordGenerator()

@pytest.fixture(autouse=True)
def setup_page(page: Page):
    pp = PasswordPage(page)
    page.goto(pp.URL)
    pp.consent_button.click()

def test_rule_0(page: Page):
    """
        Invoke error rule 1.
    """
    pp = PasswordPage(page)
    password_to_invoke_first_rule = "test"
    pp.fill_password(password_to_invoke_first_rule)
    rule_1_container = pp.rule_container(rules["rule_1_desc"])
    expect(rule_1_container, "Rule 1 should be visible but not validated").to_have_class(pp.error_class_re)

def test_rule_1(page: Page):
    """
        Pass rule 1 and invoke error rule 2.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_1_at_least_5_chars())
    rule_1_container =  pp.rule_container(rules["rule_1_desc"])
    rule_2_container =  pp.rule_container(rules["rule_2_desc"])

    expect(rule_1_container, "Rule 1 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_2_container, "Rule 2 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_2(page:Page):
    """
        Pass rule 2 and invoke error rule 3.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_2_include_number())
    rule_2_container =  pp.rule_container(rules["rule_2_desc"])
    rule_3_container =  pp.rule_container(rules["rule_3_desc"])

    expect(rule_2_container, "Rule 2 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_3_container, "Rule 3 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_3(page:Page):
    """
        Pass rule 3 and invoke error rule 4.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_3_include_uppercase())
    rule_3_container =  pp.rule_container(rules["rule_3_desc"])
    rule_4_container =  pp.rule_container(rules["rule_4_desc"])

    expect(rule_3_container, "Rule 3 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_4_container, "Rule 4 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_4(page:Page):
    """
        Pass rule 4 and invoke error rule 5.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_4_include_special_char())
    rule_4_container =  pp.rule_container(rules["rule_4_desc"])
    rule_5_container =  pp.rule_container(rules["rule_5_desc"])

    expect(rule_4_container, "Rule 4 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_5_container, "Rule 5 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_5(page:Page):
    """
        Pass rule 5 and invoke error rule 6.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_5_add_up_to_25())
    rule_5_container =  pp.rule_container(rules["rule_5_desc"])
    rule_6_container =  pp.rule_container(rules["rule_6_desc"])

    expect(rule_5_container, "Rule 5 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_6_container, "Rule 6 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_6(page:Page):
    """
        Pass rule 6 and invoke error rule 7.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_6_include_month_name())
    rule_6_container =  pp.rule_container(rules["rule_6_desc"])
    rule_7_container =  pp.rule_container(rules["rule_7_desc"])

    expect(rule_6_container, "Rule 6 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_7_container, "Rule 7 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_7(page:Page):
    """
        Pass rule 7 and invoke error rule 8.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_7_include_roman_numeral())
    rule_7_container =  pp.rule_container(rules["rule_7_desc"])
    rule_8_container =  pp.rule_container(rules["rule_8_desc"])

    expect(rule_7_container, "Rule 7 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_8_container, "Rule 8 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_8(page:Page):
    """
        Pass rule 8 and invoke error rule 9.
    """
    password = pg.pass_rule_7_include_roman_numeral()
    pp = PasswordPage(page)
    pp.fill_password(password)
    sponsors_qnt = page.locator(".sponsor").count()
    get_sponsor_index = random.randint(0, sponsors_qnt-1)
    sponsor = page.locator("img.sponsor").nth(get_sponsor_index).get_attribute("class").split(' ')[-1]

    pp.fill_password(password + sponsor)
    rule_8_container =  pp.rule_container(rules["rule_8_desc"])
    rule_9_container =  pp.rule_container(rules["rule_9_desc"])
    
    expect(rule_8_container, "Rule 8 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_9_container, "Rule 9 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_9(page:Page):
    """
        Pass rule 9 and invoke error rule 10.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_9_multiply_roman_up_to_35())
    rule_9_container =  pp.rule_container(rules["rule_9_desc"])
    rule_10_container =  pp.rule_container(rules["rule_10_desc"])

    expect(rule_9_container, "Rule 9 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_10_container, "Rule 10 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_10(page:Page):
    """
        Pass rule 10 and invoke error rule 11.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_9_multiply_roman_up_to_35())
    pp.fill_password(pg.pass_rule_10_include_captcha(page))
    rule_10_container =  pp.rule_container(rules["rule_10_desc"])
    rule_11_container =  pp.rule_container(rules["rule_11_desc"])

    expect(rule_10_container, "Rule 10 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_11_container, "Rule 11 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))

def test_rule_11(page:Page):
    """
        Pass rule 11 and invoke error rule 12.
    """
    pp = PasswordPage(page)
    pp.fill_password(pg.pass_rule_9_multiply_roman_up_to_35())
    pp.fill_password(pg.pass_rule_10_include_captcha(page))
    pp.fill_password(pg.pass_rule_11_include_worlde(page))
    rule_11_container =  pp.rule_container(rules["rule_11_desc"])
    rule_12_container =  pp.rule_container(rules["rule_12_desc"])

    expect(rule_11_container, "Rule 11 should be visible and validated").not_to_have_class(re.compile(pp.error_class_re))
    expect(rule_12_container, "Rule 12 should be visible but not validated").to_have_class(re.compile(pp.error_class_re))
