from bs4 import  BeautifulSoup
from selenium import webdriver


driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

table = soup.find('table', class_ = 'chart')

for td in table.find_all('td', class_ = 'titleColumn'):
	print(td.text.strip().replace('\n','').replace('      ',''))