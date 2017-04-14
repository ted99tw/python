import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://search.ruten.com.tw/search/s000.php?enc=u&searchfrom=searchf&k=sg90&c=0011'

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

res = requests.get(url, headers=headers)

browser = webdriver.PhantomJS(executable_path='./phantomjs')
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

result = soup.select('.results-listing')[0]

items = result.select('.media-body')

data = []

for item in items:
	data.append((
		int(item.select('.rt-text-price')[0].text.replace(',','')),
		item.select('.item-name-anchor')[0]['href'],
		item.select('.item-name-text')[0].text
	))

sortdate = []
sorteddata = sorted(data, key=lambda student: student[0])
for d in sorteddata:
	print(str(d[0])+' '+d[2])



