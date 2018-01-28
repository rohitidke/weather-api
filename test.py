from flask import Flask, render_template, request
import requests

app= Flask(__name__)

@app.route('/temp',methods=['post'])
def temp():
	zipcode= request.form['zip']
	r= requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',in&appid=00259126402314347806eeaf3b69dee0')
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_c = (temp_k - 273.15)
	return render_template('temp.html',temp=temp_c)


@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)
