from django.shortcuts import render

from django.http import HttpResponse
'''
def function1(request): # this is the object of HttpResponse
	data = "<html> <body> <h1> Hello All </h1> </body> </html>"
	return HttpResponse(data)


def function2(request): # this is the object of HttpResponse
	data = "<html> <body> <h1> Home Page </h1> </body> </html>"
	return HttpResponse(data)

# Create your views here.
'''

def function1(request): # this is the object of HttpResponse
	
	return render(request, 'blog/home.html')


def function2(request): # this is the object of HttpResponse
	data = "<html> <body> <h1> Home Page </h1> </body> </html>"
	return HttpResponse(data)

