from flask import Flask,request
import mysql.connector as mysql
import os 

app = Flask(__name__)

##cnx = connection.MySQLConnection(user='root', password='js3210',
##                                 host='localhost',
##                                 database='embodyvr')

@app.route('/users',methods=['GET'])
def user():
    try:
      conn = mysql.connect(host = "172.17.0.1",user = "root",password = "supersecret",database="embodyvr",port=3306)
      cursor = conn.cursor()
      user=request.args.get('user')
      query = ("SELECT user_key FROM users where user=%s")
      cursor.execute(query,(str(user),))
      result=cursor.fetchone()
      if result == None:
        raise Exception("400 error")
      else:
        user_key=str(result[0])
        cursor.close()
        # if len(user_key)==0:
          # raise Exception("400 Error No key found")
        #print("connected")
        conn.close()
    except Exception as e:
      user_key=str(e)
    return "request from port: "+str(os.environ['MESSAGE'])+" user key value= "+user_key
  
@app.route('/')
def index():
  return 'Hello from Server'
##cnx.close()
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
