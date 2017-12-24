from flask import Flask, render_template
from flask import request
import pymysql
import re
import cseindex
import dseindex
app = Flask(__name__)

conn = pymysql.connect(host='localhost', user='root', passwd='hellothere', db='stk')
cur = conn.cursor()

@app.route('/')
def runpy():
    cse = cseindex.main()
    dse = dseindex.main()
    return render_template('index.html',cse=cse,dse=dse)

@app.route('/prediction')
def predict():
    res = {}
    query = "SELECT * from predicted"
    ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
    try:
        cur.execute(query)
        results = cur.fetchall()
        for result in results:
            cur.execute(ltpquery %(result[0]))
            res[result[0]] = cur.fetchone()[0]
    except Exception as e:
        print(e)
    print(res)
    return render_template('prediction.html',result=results,ress=res)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction',methods=['POST'])
def prediction():
    res = {}
    stock = request.form['market']
    stocktype = request.form['type']
    radiovalue = request.form['optradio']
    print(stock)
    print(stocktype)
    print(radiovalue)
    if(stock=='dse' and stocktype=='general'):
        if(radiovalue=='0'):
            query = "SELECT * from predicted"
            ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
            except Exception as e:
                print(e)
            print(res)
            return render_template('prediction.html',result=results,ress=res)

        elif(radiovalue=='1'):
            query = "SELECT * from predicted"
            ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 0 and val<=50):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

        elif(radiovalue=='2'):
            query = "SELECT * from predicted"
            ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 51 and val<=100):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

        elif(radiovalue=='3'):
            query = "SELECT * from predicted"
            ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 101 and val<= 150):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

        elif(radiovalue=='4'):
            query = "SELECT * from predicted"
            ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 151 and val<= 200):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

    
    elif(stock=='dse' and stocktype=='featured'):
        toplist = ['APEXFOOT','ACI','AAMRATECH','ARAMIT','BEXIMCO','BSRMSTEEL','LANKABAFIN','NORTHERN','RENATA','SAMORITA','STYLECRAFT','HEIDELBCEM','IBNSINA','BBSCABLES','LINDEBD','GP']
        query = "SELECT * from predicted WHERE `name`='%s'"
        ltpquery = "SELECT `LTP*` FROM dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
        try:
            results = []
            for name in toplist:
                cur.execute(query %(name))
                results.append(cur.fetchone())
            print(results)
            for result in results:
                cur.execute(ltpquery %(result[0]))
                res[result[0]] = cur.fetchone()[0].replace(',','')
        except Exception as e:
            print(e)
        return render_template('prediction.html',result=results,ress=res)


    elif(stock=='cse' and stocktype=='general'):
        if(radiovalue=='0'):
            query = "SELECT * from csepredicted"
            ltpquery = "SELECT `LTP*` FROM csedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
            except Exception as e:
                print(e)
            print(res)
            return render_template('prediction.html',result=results,ress=res)

        elif(radiovalue=='1'):
            query = "SELECT * from csepredicted"
            ltpquery = "SELECT `LTP*` FROM csedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 0 and val<=50):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

        elif(radiovalue=='2'):
            query = "SELECT * from csepredicted"
            ltpquery = "SELECT `LTP*` FROM csedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 51 and val<=100):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

        elif(radiovalue=='3'):
            query = "SELECT * from csepredicted"
            ltpquery = "SELECT `LTP*` FROM csedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 101 and val<= 150):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

        elif(radiovalue=='4'):
            query = "SELECT * from csepredicted"
            ltpquery = "SELECT `LTP*` FROM csedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
            try:
                cur.execute(query)
                results = cur.fetchall()
                for result in results:
                    cur.execute(ltpquery %(result[0]))
                    res[result[0]] = cur.fetchone()[0]
                sorted_res = {}
                for key,val in res.items():
                    val = float(val)
                    if(val >= 151 and val<= 200):
                        sorted_res[key] = val
            except Exception as e:
                print(e)
            print(sorted_res)
            return render_template('prediction.html',result=results,ress=sorted_res)

    
    elif(stock=='cse' and stocktype=='featured'):
        toplist = ['ACIFORMULA','AFTABAUTO','AMCL(PRAN)','APEXFOOT','BATASHOE','DUTCHBANGL','GP','IBBLPBOND','MARICO',
        'NTC','PADMAOIL','PENINSULA','RECKITTBEN','SQURPHARMA','WATACHEM']
        query = "SELECT * from csepredicted WHERE `name`='%s'"
        ltpquery = "SELECT `LTP*` FROM csedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE`"
        try:
            results = []
            for name in toplist:
                cur.execute(query %(name))
                results.append(cur.fetchone())
            print(results)
            for result in results:
                cur.execute(ltpquery %(result[0]))
                res[result[0]] = cur.fetchone()[0].replace(',','')
        except Exception as e:
            print(e)
        return render_template('prediction.html',result=results,ress=res)

@app.route('/search',methods=['GET','POST'])
def form_post():
    text = request.args.get('search')
    test = []
    query = "SELECT * from dsedayendsumm WHERE `TRADING CODE`='%s' ORDER BY `DATE` ASC"
    try:
        cur.execute(query % (text.upper()))
        results = cur.fetchall()
    except Exception as e:
        print(e)
    return render_template('searchResult.html',result=results)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
