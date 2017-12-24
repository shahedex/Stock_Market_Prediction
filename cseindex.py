import pymysql
import re

conn = pymysql.connect(host='localhost', user='root', passwd='hellothere', db='stk')
cur = conn.cursor()

query = "SELECT * from csedayendsumm"
try:
    cur.execute(query)
    results = cur.fetchall()
except Exception as e:
    print(e)

dates = []
for res in results:
    dates.append(res[1])
dates = set(dates)

def current_mcap(date):
    total_mcap = 0
    query = "SELECT * from csedayendsumm WHERE `DATE`='%s'"
    cur.execute(query %(date))
    results = cur.fetchall()
    mcap = 0
    for result in results:
        mcap += (float(result[3].replace(',','')) * float(result[10].replace(',','')))
    total_mcap += mcap
    return total_mcap

def closing_mcap(date):
    total_mcap = 0
    query = "SELECT * from csedayendsumm WHERE `DATE`='%s'"
    cur.execute(query %(date))
    results = cur.fetchall()
    mcap = 0
    for result in results:
        mcap += (float(result[7].replace(',','')) * float(result[10].replace(',','')))
    total_mcap += mcap
    return total_mcap

def main(dates=dates):
    dates = sorted(list(dates))
    del dates[0]
    index = []
    yesterdays = 1430
    for date in range(len(dates)):
        print(dates[date])
        current = current_mcap(dates[date])
        closing = closing_mcap(dates[date])
        current_index = (yesterdays*current)/current
        closing_index = (yesterdays*closing)/current
        yesterdays = closing_index
        index.append([dates[date],format(current_index,'0.2f')])
    return index

if __name__ == '__main__':
    ins = main()
    print(ins)
    