from django.shortcuts import render, redirect, get_object_or_404
from .forms import AttForm
from .forms1 import StuForms, MarkAtt,CheckAttForm,MasterDataForm, Mark_AttendanceForm,CheckAttClassForm,CheckAttForm
from .models import Student,Master_data,Mark_Attendance4 as m4
import time 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from .decorators import allowed_users

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
	context = {'data': Master_data.objects.all(), "get1" : "Attendance of all the student "}
	return render(request, "attendance/display_data.html", context)

def checkOneform(request):
	fm = CheckAttForm(request.POST)
	if fm.is_valid():
		roll1=fm.cleaned_data['id']
		return redirect("checkone",roll=roll1)
	fm = CheckAttForm()
	return render(request, "attendance/display.html", {'form':fm})


def CheckOne(request,roll):
	context = {'data': Student.objects.filter(stuid=roll), "get1" : f"Attendance of the {roll} "}
	return render(request, "attendance/display_data.html", context)

@login_required(login_url='login')
def MasterDataEnter(request):
	form = MasterDataForm()
	context = {'form':form, "legend": "Enter the data"}
	if request.method == 'POST':
		form = MasterDataForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Added")
			return redirect("profile")
	return render(request,"attendance/form_display.html", context)

def e_h(t1):
	t9 = time.localtime(t1)
	return time.strftime('%d-%m-%Y-%H',t9)

def MarkAtt(request):
	form = Mark_AttendanceForm()
	context = {'form':form}

	if request.method == 'POST':
		print ("AAAAAAA")
		form = Mark_AttendanceForm(request.POST)
		print ("BBBBBBBBBBBBBBBB")
		if form.is_valid():
			try :
				print ("cccccc", form)
				mark1 =form.save(commit=False)
				mark1.ip_address  = request.META.get('REMOTE_ADDR')
				mark1.platform = request.META.get('HTTP_USER_AGENT')
				mark1.time1 = int(time.time())
				mark1.date1 = e_h(mark1.time1)
				mark1.Master1 = get_object_or_404(Master_data,roll_number=mark1.roll_number)
				mark1.class_name = mark1.class_name.upper()
				mark1.save()
				messages.success(request,"Attendance Marked")
			except IntegrityError:
				messages.warning(request, "Duplicate Entry ")
			except Exception as e :
				print (e)
				messages.warning(request,type(e))

	return render(request, "attendance/form_display.html", context)

# this one only for one specific grp 
@login_required(login_url='login')
@allowed_users(allowed_roles=['grp2']) # grp2 teachers
def ClassAttendance(request):
	form = CheckAttClassForm()
	context = {'form':form}
	if request.method=='POST':
		form = CheckAttClassForm(request.POST)
		print ("aaaa", form)
		if form.is_valid():
			c1=form.cleaned_data['classname']
			print ("**&*&(&",c1)
			data = m4.objects.filter(class_name=c1)
			context = {"data":data}
			return render(request, "attendance/display_data_att.html", context)

	return render(request, "attendance/form_display.html", context)

# this for one grp
@login_required(login_url='login')  # grp1  = student
@allowed_users(allowed_roles=['grp1','grp2'])
def CheckAttOne(request):
	form = CheckAttForm()
	context = {"form": form, "get1" : f"Your Attendance"}
	if request.method=='POST':
		form = CheckAttForm(request.POST)
		print ("jjjj", form)
		if form.is_valid():
			roll=form.cleaned_data.get('id')
			context = {'data': m4.objects.filter(roll_number=roll), "get1" : f"Attendance of the {roll} "}
	return render(request, "attendance/display_form_att.html", context)


########################################################
from .serializers import AttSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse 
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
'''
def Student_details(request,pk):
	try :
		stu = Student.objects.get(id=pk) # model complex object 
		serializer = AttSerializer(stu) 
		json_data = JSONRenderer().render(serializer.data)
		print (json_data)

	except Exception as e :
		print (e)
		json_data = '{"Not get": "NIL"}'
	return HttpResponse(json_data,content_type='application/json')
@csrf_exempt
def student_api(request):
	if request.method =="POST":
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = AttSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': "Data Created"}
			return JsonResponse(res,safe=False)
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application/json')

	if request.method =='PUT':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('stuid')
		stu = Student.objects.get(stuid=id)
		serializer = AttSerializer(stu, data=pythondata,partial=True)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': "Data Created"}
			return JsonResponse(res,safe=False)
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application/json')

	if request.method =='DELETE':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('stuid')
		stu = Student.objects.get(stuid=id)
		stu.delete()
		res = {'msg': "deleted"}
		return JsonResponse(res,safe=False)

##################################
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def hello_world(request):
	if request.method =='GET':
		return Response({'msg': "This is a GET response"})

	if request.method == 'POST':
		print ("hello", repr(request.data))
		#print("it" ,dir(request))

		return Response({'msg': "This is a POST request"})



'''
####################################################
########## Generic class API
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
class StudentListAPI(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = AttSerializer
	#authentication_classes=[BasicAuthentication]
	#permission_classes=[IsAuthenticated]
	#permission_classes=[IsAdminUser]

from rest_framework.generics import RetrieveAPIView
class StudentRetrieveAPI(RetrieveAPIView):
	queryset = Student.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import CreateAPIView
class StudentCreateAPI(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import UpdateAPIView
class StudentUpdateAPI(UpdateAPIView):
	queryset = Student.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import DestroyAPIView
class StudentDestroyAPI(DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = AttSerializer

########################### API Authentication #####################
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,DjangoModelPermissions
from .permissions import MohitPermission
class StudentListCreateAPI(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = AttSerializer
	#authentication_classes=[BasicAuthentication]
	#authentication_classes=[SessionAuthentication]
	################Permission###############
	#permission_classes=[IsAdminUser]
	#permission_classes=[IsAuthenticatedOrReadOnly]
	#permission_classes = [DjangoModelPermissions]
	#permission_classes = [MohitPermission]
