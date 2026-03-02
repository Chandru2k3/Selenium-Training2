import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)


def setup():
    driver = webdriver.Chrome(opts)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver

class TestRegister:

    def test_register_link(self,setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self,setup):
        setup.find_element('id', 'gender-male').click()

    def test_firstname(self,setup):
        setup.find_element('id', 'FirstName').send_keys('Lolla')

    def test_lastname(self,setup):
        setup.find_element('id', 'LastName').send_keys('Venkat')

    def test_reg_email(self,setup):
        setup.find_element('id', 'Email').send_keys('venkat@gmail.com')

    def test_reg_password(self,setup):
        setup.find_element('id', 'Password').send_keys('venkat@12345')

    def test_confirm_pwd(self,setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('venkat@12345')
        time.sleep(2)

class TestLogin:

    def test_login_link(self,setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self,setup):
        setup.find_element('id', 'Email').send_keys('venkat@gmail.com')

    def test_login_pwd(self,setup):
        setup.find_element('id', 'Password').send_keys('venkat@12345')

