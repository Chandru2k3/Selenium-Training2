
'''
1.  Go to https://www.myntra.com/, enter adidas in the search bar, select any auto-suggestion,
    wap to print the name and price of all the shoes available (Shoename = Price)
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)


driver.get('https://www.myntra.com/')

driver.find_element('xpath','//input[@class="desktop-searchBar"]').click()
time.sleep(2)

driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('adidas')
time.sleep(2)

driver.find_element('xpath','//li[@data-index="1"]').click()

adidas = driver.find_elements('xpath','//div[@class="product-productMetaInfo"]')

for ele in adidas :
    print(ele.text)
'''
2.  Go to https://www.myntra.com/, enter adidas in the search bar, select any auto-suggestion,
    wap to print all the colors
'''
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)


driver.get('https://www.myntra.com/')

driver.find_element('xpath','//input[@class="desktop-searchBar"]').click()
time.sleep(2)

driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('adidas')
time.sleep(2)

driver.find_element('xpath','//li[@data-index="1"]').click()

driver.find_element('xpath','(//div[@class="colour-more"])/span').click()

colors = driver.find_elements('xpath','(//div[@class="vertical-filters-filters"])[2]')
for ele in colors:
    print (ele.text)
'''
3.  Go to https://in.bookmyshow.com/, select the city. wap to print all the recommended movies
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://in.bookmyshow.com/")

driver.find_element('xpath','//div[@class="sc-1jg5yz-1 dIWPfO"]').click()
time.sleep(1)

r = driver.find_elements('xpath','//div[@class="sc-lnhrs7-4 hQMAVG"]')

for ele in r:
    print(ele.text)

'''
4.  Go to https://www.zomato.com/bangalore/restaurants, search for pizza, select pizza delivery,
    choose any restaurant, wap to print the names of all the items present.
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.zomato.com/bangalore/restaurants")

driver.find_element('xpath','//input[@class="sc-dBfaGr dyyfrm"]').click()

driver.find_element('xpath','//input[@class="sc-dBfaGr dyyfrm"]').send_keys("pizza")
time.sleep(2)

driver.find_element('xpath','//div[@class="sc-glUWqk GrjUP"]').click()
time.sleep(2)

driver.find_element('xpath','//div[@class="sc-evWYkj cRThYq"]').click()
time.sleep(2)

