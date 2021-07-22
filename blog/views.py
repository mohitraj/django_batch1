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

def home(request): # this is the object of HttpResponse
	
	return render(request, 'blog/home.html', {'title': 'Batch1'})

posts = [{'author': 'Munesh', 
         'title': 'solar energy', 
         'content':'Renewable energy source', 
         'date1': 'July 22, 2021'},

         {'author': 'joel', 
         'title': 'Health', 
         'content':'Health is wealth', 
         'date1': 'July 21, 2021'},

          ]


def all_post(request):
	context = { 'posts' : posts }
	return render(request, 'blog/all_posts.html', context)

