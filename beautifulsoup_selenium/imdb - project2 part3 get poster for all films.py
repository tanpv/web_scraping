# div class_=poster --> a['href'] --> div[1] class_=pswp__zoom-wrap --> img[1]['src']

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

options = webdriver.ChromeOptions()
options.headless  = False

chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, 
						options=options)


def get_movies():
	url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'

	driver.get(url)

	# print driver.page_source

	soup = BeautifulSoup(driver.page_source,'lxml')

	table = soup.find('table', class_ = 'chart')

	movies = []

	for td in table.find_all('td', class_ = 'titleColumn'):
		
		full_title = td.text.strip().replace('\n','').replace('      ','')
		print(full_title)

		rank = full_title.split('.')[0]
		print(rank)

		title = full_title.split('.')[1].split('(')[0]
		print(title)

		year = full_title.split('(')[1][:-1]
		print(year)

		a = td.find('a')
		print(a['href'])

		print('\n')

		movie = {}
		movie['rank'] = rank
		movie['title'] = title
		movie['year'] = year
		movie['link'] = a['href']

		movies.append(movie)

	# driver.quit()

	return movies


def download_all_posters(movies):

	for movie in movies[:10]:
		url = 'http://www.imdb.com/' + movie['link']

		driver.get(url)

		soup = BeautifulSoup(driver.page_source,'lxml')

		div = soup.find('div', class_ = 'poster')

		a = div.find('a')

		# print 'http://www.imdb.com' + a['href']

		url = 'http://www.imdb.com' + a['href']

		driver.get(url)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		all_div = soup.find_all('div', class_ = 'pswp__zoom-wrap')

		all_img = all_div[1].find_all('img')

		print(all_img[1]['src'])

		poster = './imdb_posters/{0}.jpg'.format(movie['title'].replace(':',''))
		f = open(poster, 'wb')
		f.write(requests.get(all_img[1]['src']).content)
		f.close()

	driver.quit()


download_all_posters(get_movies())