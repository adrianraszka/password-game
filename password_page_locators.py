from playwright.sync_api import Page
import re
from typing import List

class PasswordPage:

    URL = "https://neal.fun/password-game/"
    error_class_re = re.compile(r"rule-error")

    def __init__(self, page: Page):
        self.page = page
        self.consent_button = page.locator("button.fc-cta-consent")
        self.password_input = page.locator("div.ProseMirror")

    def fill_password(self, password):
        self.password_input.fill(password)

    def rule_container(self, rule_text):
        return self.page.locator("div.rule", has_text=rule_text)
    