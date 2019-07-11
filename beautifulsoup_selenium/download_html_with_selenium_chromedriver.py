from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print html_doc