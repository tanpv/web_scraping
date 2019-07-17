from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)

driver.close()