from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe', options=)

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)

driver.close()