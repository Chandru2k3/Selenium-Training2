from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
#
# driver.find_element('css selector','input[name="firstname"]').send_keys("Chandrashekhar")
# time.sleep(2)
#
# driver.find_element('css selector','input[name="lastname"]').send_keys("Madelli")
# time.sleep(2)
#
# driver.find_element('css selector','input[name="reg_email__"]').send_keys("8296205572")
# time.sleep(2)
#
# driver.find_element('css selector','input[data-type="password"]').send_keys("Chandru@2k3")
# time.sleep(2)



driver.get("https://www.instagram.com/accounts/emailsignup/")




















