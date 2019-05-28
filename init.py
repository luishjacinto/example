from flask import Flask # session redirect, flash, abort, request

app = Flask(__name__)


@app.route("/")
#@app.route("/", methods=['GET','POST'])
def helloword():
    return "OLA MUNDO"

 
app.run(debug=True, port=5000)
