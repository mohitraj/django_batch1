from django.shortcuts import render, redirect
from .forms import AttForm
from .forms1 import StuForms, MarkAtt
from .models import Student
import time 
from django.contrib import messages

def AttView(request):
	if request.method== 'POST':
		fm =AttForm(request.POST)
		if fm.is_valid():
			#print ("form is valid")
			stuid1= fm.cleaned_data['stuid']
			stuname1 = fm.cleaned_data['stuname']
			stmail1 = fm.cleaned_data['stmail']
			stupass1 = fm.cleaned_data['stmail']

			reg = Student( stuid = stuid1, stuname= stuname1, stmail= stmail1,stupass= stupass1)
			reg.save()
			print ("Saved")
		
	form = AttForm()
	context = {'form': form}
	#print (dir(request))
	return render(request, 'attendance/display.html', context)

def success(request):
	return render(request, 'attendance/success.html')

def AttView1(request):
	fm = StuForms(request.POST)
	if fm.is_valid():
		fm.save()
		return redirect('success_add')
	fm = StuForms()
	return render(request, 'attendance/display.html', {"form": fm})



def attstundent(request):
	fm = MarkAtt(request.POST)
	if fm.is_valid():
		mark1=fm.save(commit=False)
		data = fm.cleaned_data.items()
		print ("Data is ", data)
		t1 = int(time.time())
		
		print ("data*******", fm.cleaned_data['name'] )
		mark1.time = t1
		#print (fm.cleaned_data.items())
		#fm.time = t1
		mark1.save()

		#return redirect('success_add')
		messages.error(request,"Attendance not Marked")

	fm = MarkAtt()
	return render(request, 'attendance/display.html', {"form": fm})

def checkall(request):
	context = {'data': Student.objects.all(), "get1" : "Attendance of all the student "}
	return render(request, "attendance/display_data.html", context)

def CheckOne(request,roll):
	context = {'data': Student.objects.filter(stuid=roll), "get1" : f"Attendance of the {roll} "}
	return render(request, "attendance/display_data.html", context)
