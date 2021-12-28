import requests
import json
'''
URL = "http://127.0.0.1:8000/att/stuinfo/11"

r = requests.get(url=URL)
data = r.json()

print (data)

'''
URL = "http://127.0.0.1:8000/att/student_api/"

def postdata():
	data = { 'stuid': 59,
		'stuname' : 'intel51',
		'stmail' : "mohit59@gmail.com",
		'stupass': 2123222

	}
	jsondata  = json.dumps(data)
	r = requests.post(url=URL, data= jsondata)
	data = r.json()
	print (data)

def putdata():
	data = { 'stuid': 78,
		'stuname' : 'Sdeep',
		'stmail' : "mohit@gmail.com",
		'stupass': 21212

	}
	jsondata  = json.dumps(data)
	r = requests.put(url=URL, data= jsondata)
	data = r.json()
	print (data)

def delete():
	data = { 'stuid': 4,


	}
	jsondata  = json.dumps(data)
	r = requests.delete(url=URL, data= jsondata)
	data = r.json()
	print (data)

postdata()


