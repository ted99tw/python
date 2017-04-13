import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU.php'
def parseTse(year,month,no):
	year = str(year)
	month = str(month)
	no = str(no)
	payload = {
		'query_year' : year,
		'query_month': month,
		'CO_ID'      : no,
		'query-button':'%E6%9F%A5%E8%A9%A2'
	}
	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	}
	res = requests.post(url, headers=headers, data=payload)
	data = res.text
	soup = BeautifulSoup(data, 'html.parser')
	content = soup.table #first table
	table = pd.read_html(str(content))[0] #the output of pd is list
	#print(table)
	with open('./'+year+'_tse_'+no+'.csv','a') as f:
		f.write(str(table.to_csv(header=False, index=False)))
for m in range(1,3):
	parseTse(2015,m,2317)
	time.sleep(2)


