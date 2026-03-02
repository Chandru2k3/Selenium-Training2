from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.kushals.com/")
time.sleep(2)

driver.find_element("partial link text","Necklaces-1").click()
time.sleep(2)

driver.find_element("partial link text","Earrings-1").click()
time.sleep(2)

driver.find_element("partial link text","Bangles").click()
time.sleep(2)

driver.find_element("partial link text","Accessories").click()
time.sleep(2)











