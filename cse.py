import re
import pymysql
import requests
from bs4 import BeautifulSoup
from datetime import datetime
# import lxml.html

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='stk')
cur = conn.cursor()

def store(L):
	cur.execute("INSERT INTO `csedayendsumm`(`DATE`, `TRADING CODE`, `LTP*`, `HIGH`, `LOW`, `OPENP*`, `CLOSEP*`,`CHANG`, `TRADE` ,`VOLUME`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",L)
	conn.commit()
	print("Updated database ...")

def getStore(allData,curDate):
	L = []
	F = []
	head = allData.find('tr', attrs={ 'bgcolor':'#abcdf0'})
	for val in head.find_all('td'):#attributes of table
		F.append(val.get_text())
	del F[0]
	print("Got all field ... ",F)
	for tr in allData.find_all('tr', attrs={ 'bgcolor':'#FFFFFF'}):#data of the table
		L.append(curDate)
		for val in tr.find_all('td'):
			L.append(val.get_text())
			# L.append(val.get_text())
		# del L[8]		
		del L[1]	
		print(L)
		store(L)
		L.clear()
	print("Got data  ...\n")

def crawlDate():
	url="http://cse.com.bd/companyDetails.php?scriptCode=MUpBTkFUQU1G"
	html = requests.get(url)
	print("Downloaded ...\n")
	soup = BeautifulSoup(html.text, "lxml")
	allData = soup.find('td', attrs={ 'width':'436'})
	wz=allData.find_all('tr')
	cz=wz[1].find_all('td')
	curDate=cz[1].get_text()
	curDate= re.sub('[,]','',curDate)
	dt= datetime.strptime(curDate,'%b %d %Y')


	marStat= soup.find('div',attrs={ 'class':'HeaderRight'})
	marStat=marStat.find('span')
	marStat=marStat.find('b')
	return dt.date(),marStat.get_text()
	# for cell in soup.select('.RightColInner > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)'):
	# 	print(cell.prettify)
	# tree= html.fromstring(html.content)
	# /div/div[2]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]
	# tree = lxml.html.parse(url)
	# for row in tree.xpath('/html/body/div/div/div[5]'):
	# 	print(row)
	# tree=lxml.html.HTML(response.text)
	# print("osdfdfdfd")


def crawl(url):
	date, marketStatus= crawlDate();
	if(marketStatus!="Closed"):
		print("Sorry market is open.. Try again after market is closed.")
		return
	html = requests.get(url)
	print("Downloaded ...\n")
	soup = BeautifulSoup(html.text, "lxml")
	# print(soup.prettify)
	allData = soup.find('table', attrs={ 'id':'report'})
	# print(allData.prettify)
	print("Soup ...\n")
	getStore(allData,date)



if __name__ == '__main__':
	url="http://cse.com.bd/current_share_price_tc.php"
	crawl(url)