from flask import Flask,request
import os
app = Flask(__name__)

users={"abc":123,"man":"mankey","dog":"dogkey","cat":"catkey"}
@app.route('/user',methods=['GET'])
def user():
	try:
		user=request.args.get('user')
		return "response from "+str(os.environ['MESSAGE'])+" key for given user:"+str(users[user]) 
	except Exception as e:
		return "400 Key Error"+str(e)
if __name__ == "__main__":
    app.run(port=5000,host='0.0.0.0',debug=True)
