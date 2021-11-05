from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import SignUP,UserUpdateForm, ProfileUpdateForm
from .models import myProfile
from django.contrib.auth.models import User
@login_required
def profile(request):
	return render(request, 'user_app/profile.html')



def login_page(request):

	next =''
	if request.GET:
		next = request.GET['next']
	if request.method == "POST":
		user1 = request.POST.get("username")
		pass1 = request.POST.get("password")

		user = authenticate(request, username=user1, password=pass1)
		print ("User", user)
		if user is not None:
			login(request,user)
			if next=="":
				return redirect('profile')
			else:
				return redirect(next)


	form = AuthenticationForm()
	context = {'form': form, 'legend' : "Login NOW"}
	return render(request, 'user_app/login.html', context )



def register(request):

	if request.method=='POST':
		form = SignUP(request.POST)
		if form.is_valid():
			form.save()
			user1 = form.cleaned_data.get("username")
			messages.success(request, f"Account is  created for {user1}")
			myProfile.objects.create(user=user1)
			return redirect("login")

	form = SignUP()
	context = {'form': form, 'legend' : "Register Today"}
	return render(request, 'user_app/login.html', context )


# change password view 
def UserChangePass(request):

	if request.method == 'POST':
		fm = PasswordChangeForm(user=request.user ,data= request.POST)
		if fm.is_valid():
			fm.save()
			update_session_auth_hash(request,fm.user)
			messages.success(request, "Password Changed Successfully")
			return redirect('profile')


	fm = PasswordChangeForm(user=request.user)
	context = {'form': fm, 'legend':"Change password"}
	return render(request,'user_app/login.html', context)

# Create your views here.
def UpdateProfile(request):
	try:
		if request.method == 'POST':
				u_form = UserUpdateForm(request.POST,instance=request.user)
				p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.myprofile )
				if u_form.is_valid() and p_form.is_valid():
					u_form.save()
					p_form.save()
					messages.success(request,"Profile Updated")
					return redirect('profile')

		else:
			u_form = UserUpdateForm(instance=request.user)
			p_form = ProfileUpdateForm(instance=request.user.myprofile )
			context = {'u_form': u_form, 'p_form' : p_form, 'legend' :"Update Form "}
			return render (request,'user_app/upprofile.html', context)
	except User.myprofile.RelatedObjectDoesNotExist:
		myProfile.objects.create(user=request.user)
	except Exception as e :
		print (e, type(e))