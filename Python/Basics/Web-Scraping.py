from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('url')

# accessing dom elements
driver.find_elements_by_xpath('//table/thead or tbody/tr') # accessing tables
driver.find_elements_by_name('name')
driver.find_elements_by_id(id_='id')
driver.find_elements_by_class_name('name')
driver.find_elements_by_css_selector('css_selector')

# end scrapping
driver.close()
