from bs4 import  BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless  = True
driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', 
						options=options)

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')
print(soup.prettify())

table = soup.find('table', class_ = 'chart')
for td in table.find_all('td', class_ = 'titleColumn'):
	print(td.text.strip().replace('\n','').replace('      ',''))





