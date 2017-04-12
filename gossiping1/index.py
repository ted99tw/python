import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
payload = {
	'from' : '/bbs/Gossiping/index.html',
	'yes' : 'yes'	
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18',data=payload,headers=headers)

pagelinkurl = 'https://www.ptt.cc/bbs/Gossiping/index.html'

#最多5頁
for i in range(0,5):
	print('========== '+str(i)+' th page'+' ========== : '+pagelinkurl)
	res = rs.get(pagelinkurl,headers=headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	items = soup.select('.r-ent')
	for item in items:
		print('{} {}{}'.format(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text))

	#找上一頁連結，找不到就break
	pagelinkurl = ''
	pagelinks = soup.select('a[href^="/bbs/Gossiping/"]')
	for link in pagelinks:
		if '上頁' in str(link.string):
			pagelinkurl = 'https://www.ptt.cc'+link['href']
			break;
	if len(pagelinkurl)	== 0:
		break;	


	