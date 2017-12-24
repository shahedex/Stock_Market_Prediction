import pymysql
import requests
from bs4 import BeautifulSoup

conn = pymysql.connect(host='localhost', user='root', passwd='hellothere', db='stk')
cur = conn.cursor()

def getUrl(dir):
	url=open(dir,"r").read()
	return url

def store(F,L):
	cur.execute("INSERT INTO `dsedayendsumm`(`DATE`, `TRADING CODE`, `LTP*`, `HIGH`, `LOW`, `OPENP*`, `CLOSEP*`, `YCP`, `TRADE`, `VALUE (mn)`, `VOLUME`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",L)
	conn.commit()
	print("Updated database ...")

def getStore(allData):
	L = []
	F = []
	head = allData.find('tr', attrs={ 'bgcolor':'#D6D6D6'})
	for val in head.find_all('font'):#attributes of table
		F.append(val.get_text())
	del F[0]
	print("Got all field ... ",F)
	for tr in allData.find_all('tr', attrs={ 'bgcolor':'#FFFFFF'}):#data of the table
		for val in tr.find_all('font'):
			L.append(val.get_text())
			# L.append(val.get_text())		
		del L[0]	
		print(L)
		store(F,L)
		L.clear()
	print("Got data 1 ...\n")
	for tr in allData.find_all('tr', attrs={ 'bgcolor':'#EFEFEF'}):#data of the table
		for val in tr.find_all('font'):
			L.append(val.get_text())
		del L[0]
		print(L)
		store(F,L)
		L.clear()
	print("Got data 2 ...\n")

def crawl(url):
	# url = getUrl("dse1.txt")	
	html = requests.get(url)
	print("Downloaded ...\n")
	soup = BeautifulSoup(html.text, "lxml")
	# print(soup.prettify)
	allData = soup.find('table', attrs={ 'bgcolor':'#808000'})
	print("Soup ...\n")
	getStore(allData)

def fetchInput():
	# startDate = input("Start Date: ")
	# startMonth =input("Start Month: ")
	# startYear = input("Start Year: ")

	# endDate = input("End Date: ")
	# endMonth = input("End Month: ")
	# endYear = input("End Year: ")
	startDate="29"
	startMonth="10"
	startYear="2017"

	endDate="13"
	endMonth="12"
	endYear="2017"

	currentYear="2017"
	

	s1=startYear+"-"+startMonth+"-"+startDate
	s2=endYear+"-"+endMonth+"-"+endDate
	w1="http://www.dsebd.org/day_end_archive.php?DayEndSumDate1="
	w1=w1+s1+"&DayEndSumDate1_aut=&DayEndSumDate1_da1=&DayEndSumDate1_da2=&DayEndSumDate1_day="+startDate+"&DayEndSumDate1_dis=&DayEndSumDate1_dp=1&DayEndSumDate1_fmt=j%20F%20Y&DayEndSumDate1_frm=&DayEndSumDate1_hdt=1000&DayEndSumDate1_hid=1&DayEndSumDate1_inp=1&DayEndSumDate1_int=1&DayEndSumDate1_month="+startMonth+"&DayEndSumDate1_och=&DayEndSumDate1_pr1=&DayEndSumDate1_pr2=&DayEndSumDate1_prv=&DayEndSumDate1_pth=calendar%2F&DayEndSumDate1_rtl=&DayEndSumDate1_sna=1&DayEndSumDate1_spd=%5B%5B%5D%2C%5B%5D%2C%5B%5D%5D&DayEndSumDate1_spt=0&DayEndSumDate1_str=0&DayEndSumDate1_tar=&DayEndSumDate1_wks=&DayEndSumDate1_year="+startYear+"&DayEndSumDate1_year_end="+endYear+"&DayEndSumDate1_year_start=2015&DayEndSumDate2="+s2+"&DayEndSumDate2_aut=&DayEndSumDate2_da1=&DayEndSumDate2_da2=&DayEndSumDate2_day="+s2+"&DayEndSumDate2_dis=&DayEndSumDate2_dp=1&DayEndSumDate2_fmt=j%20F%20Y&DayEndSumDate2_frm=&DayEndSumDate2_hdt=1000&DayEndSumDate2_hid=1&DayEndSumDate2_inp=1&DayEndSumDate2_int=1&DayEndSumDate2_month="+endDate+"&DayEndSumDate2_och=&DayEndSumDate2_pr1=&DayEndSumDate2_pr2=&DayEndSumDate2_prv=&DayEndSumDate2_pth=calendar%2F&DayEndSumDate2_rtl=&DayEndSumDate2_sna=1&DayEndSumDate2_spd=%5B%5B%5D%2C%5B%5D%2C%5B%5D%5D&DayEndSumDate2_spt=0&DayEndSumDate2_str=0&DayEndSumDate2_tar=&DayEndSumDate2_wks=&DayEndSumDate2_year="+endMonth+"&DayEndSumDate2_year_start=2015&Symbol=All%20Instrument&ViewDayEndArchive=View%20Day%20End%20Archive"
	# print(w1)


	# q1=("http://www.dsebd.org/day_end_archive.php?DayEndSumDate1=%s&DayEndSumDate1_aut=&DayEndSumDate1_da1=&DayEndSumDate1_da2=&DayEndSumDate1_day=%s&DayEndSumDate1_dis=&DayEndSumDate1_dp=1&DayEndSumDate1_fmt=j%%20F%20Y&DayEndSumDate1_frm=&DayEndSumDate1_hdt=1000&DayEndSumDate1_hid=1&DayEndSumDate1_inp=1&DayEndSumDate1_int=1&DayEndSumDate1_month=%s&DayEndSumDate1_och=&DayEndSumDate1_pr1=&DayEndSumDate1_pr2=&DayEndSumDate1_prv=&DayEndSumDate1_pth=calendar%%2F&DayEndSumDate1_rtl=&DayEndSumDate1_sna=1&DayEndSumDate1_spd=%5B%5B%5D%2C%5B%5D%2C%5B%5D%5D&DayEndSumDate1_spt=0&DayEndSumDate1_str=0&DayEndSumDate1_tar=&DayEndSumDate1_wks=&DayEndSumDate1_year=%s&DayEndSumDate1_year_end=%s&DayEndSumDate1_year_start=2015&DayEndSumDate2=%s&DayEndSumDate2=%s&DayEndSumDate2_aut=&DayEndSumDate2_da1=&DayEndSumDate2_da2=&DayEndSumDate2_day=%s&DayEndSumDate2_dis=&DayEndSumDate2_dp=1&DayEndSumDate2_fmt=j%%20F%20Y&DayEndSumDate2_frm=&DayEndSumDate2_hdt=1000&DayEndSumDate2_hid=1&DayEndSumDate2_inp=1&DayEndSumDate2_int=1&DayEndSumDate2_month=%s&DayEndSumDate2_och=&DayEndSumDate2_pr1=&DayEndSumDate2_pr2=&DayEndSumDate2_prv=&DayEndSumDate2_pth=calendar%%2F&DayEndSumDate2_rtl=&DayEndSumDate2_sna=1&DayEndSumDate2_spd=%5B%5B%5D%2C%5B%5D%2C%5B%5D%5D&DayEndSumDate2_spt=0&DayEndSumDate2_str=0&DayEndSumDate2_tar=&DayEndSumDate2_wks=&DayEndSumDate2_year=%s&DayEndSumDate2_year_start=2015&Symbol=All%20Instrument&ViewDayEndArchive=View%20Day%%20End%20Archive" )#%(s1,startDate,startMonth,startYear,endYear,currentYear,s2,endDate,endMonth,endYear))

	# try:
	# 	print(q1 % (s1,startDate,startMonth,startYear,endYear,currentYear,s2,endDate,endMonth))
	# except Exception as et:
	# 	print(et)

	q1=w1
	return q1;


if __name__ == '__main__':
	url=fetchInput()
	crawl(url)
	cur.close()
	conn.close()