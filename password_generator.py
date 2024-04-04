from datetime import datetime
import string
import random
import re
import requests

# from playwright.sync_api import Page, expect

class PasswordGenerator:
    __lowercase_letters: list = list(string.ascii_lowercase)
    __uppercase_letters: list = list(string.ascii_uppercase)
    __digits: list = list(string.digits)
    __special_signs: list = list(string.punctuation)
    __months: list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    __roman_1_to_10: list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    __roman_numerals: list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    __password: str = 'aaaaa1A!2aprilIpepsiVVIIx6b5mplait'

    def __init__(self):
        pass

    def generate_string_of_numbers_to_sum_25(self, existing_sum_of_digits) -> str:
        if existing_sum_of_digits > 25:
            raise ValueError("Sum of digits in the password already exceeds 25, try again!")
        
        numbers = []
        total = existing_sum_of_digits
        while total < 25:
            num = random.randint(1, 9)
            temp = total + num
            if temp > 25:
                pass
            else:
                total += num
                numbers.append(num)
            if total == 25:
                return ''.join(str(x) for x in numbers)

    def password_digits_sum(self, password) -> int:
        return sum(int(char) for char in password if char.isdigit())
    
    def remove_digits_from_password(self, password) -> str:
        return ''.join(char for char in password if not char.isdigit())

    def pass_rule_1_at_least_5_chars(self) -> str:
        return ''.join(random.choice(self.__lowercase_letters) for _ in range(5))
    
    def pass_rule_2_include_number(self) -> str:
        previous_password = self.pass_rule_1_at_least_5_chars()
        return previous_password + random.choice(self.__digits)

    def pass_rule_3_include_uppercase(self) -> str:
        previous_password = self.pass_rule_2_include_number()
        uppercase_letter = random.choice(self.__uppercase_letters)

        while uppercase_letter in self.__roman_numerals:
            uppercase_letter = random.choice(self.__uppercase_letters)

        return previous_password + uppercase_letter

    def pass_rule_4_include_special_char(self) -> str:
        previous_password = self.pass_rule_3_include_uppercase()
        return previous_password + random.choice(self.__special_signs)

    def pass_rule_5_add_up_to_25(self) -> str:
        previous_password = self.pass_rule_4_include_special_char()
        existing_sum_of_digits = self.password_digits_sum(previous_password)
        return previous_password + self.generate_string_of_numbers_to_sum_25(existing_sum_of_digits)

    def pass_rule_6_include_month_name(self) -> str:
        previous_password = self.pass_rule_5_add_up_to_25()
        return previous_password + random.choice(self.__months)

    def pass_rule_7_include_roman_numeral(self) -> str:
        return "I" + self.pass_rule_6_include_month_name()

    def pass_rule_8_include_sponsor(self) -> str:
        return self.pass_rule_7_include_roman_numeral() + "pepsi"
    
    def pass_rule_9_multiply_roman_up_to_35(self) -> str:
        previous_password = self.pass_rule_8_include_sponsor()
        return previous_password + "XXXV"

    def pass_rule_10_include_captcha(self, page) -> str:
        previous_password = self.pass_rule_9_multiply_roman_up_to_35()

        pattern = r'captchas/(.*?)\.png'
        captcha_src = page.locator('img.captcha-img').get_attribute("src")
        captcha_text = re.search(pattern, captcha_src).group(1)
        password_without_digits = self.remove_digits_from_password(previous_password)
        password_with_captcha = password_without_digits + captcha_text
        existing_sum_of_digits = self.password_digits_sum(password_with_captcha)
        new_password = password_with_captcha + self.generate_string_of_numbers_to_sum_25(existing_sum_of_digits)
        return new_password

    def pass_rule_11_include_worlde(self, page) -> str:
        previous_password = self.pass_rule_10_include_captcha(page)

        current_date = datetime.now().strftime('%Y-%m-%d')
        url = f"https://www.nytimes.com/svc/wordle/v2/{current_date}.json"
        response = requests.get(url)
        solution = response.json()["solution"]

        return previous_password + solution

if __name__ == "__main__":
    pg = PasswordGenerator()
    print(pg.pass_rule_11())
