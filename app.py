from flask import Flask, render_template, request, flash, url_for, redirect, session
from mobile_data_strategy import DataPackage, ais_package, true_package, dtac_package
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        data = request.form.to_dict()
        DataPackage(data,ais_package)
    return render_template("index.html", ais = DataPackage(data,ais_package), trueP = DataPackage(data,true_package), dtac = DataPackage(data,dtac_package))
app.run(debug=True)



