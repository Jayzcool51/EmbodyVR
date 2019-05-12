from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! "+str(os.environ['MESSAGE'])

if __name__ == "__main__":
    app.run(port=5000,host='0.0.0.0',debug=True)
