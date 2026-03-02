from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/books")
time.sleep(2)

driver.find_element("link text","Register").click()
time.sleep(2)

driver.find_element("link text","Log in").click()




