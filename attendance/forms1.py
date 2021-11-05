from django import forms
from .models import Student, Att,Master_data, Mark_Attendance4 as Mark_Attendance
class StuForms(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Student
		fields= ['stuid', 'stuname', 'stmail', 'password']


class MarkAtt(forms.ModelForm):
	class Meta:
		model = Att
		fields = ['name']


class CheckAttForm(forms.Form):
	#label = forms.FieldType()
	id = forms.IntegerField(label= "ROLL")

class CheckAttClassForm(forms.Form):
	#label = forms.FieldType()
	classname = forms.CharField(label= "Class")


class MasterDataForm(forms.ModelForm):
	class Meta:
		model = Master_data
		#fields = ['roll_number', "name", "email", "class_name"]
		fields = "__all__"

class Mark_AttendanceForm(forms.ModelForm):
	class Meta:
		model = Mark_Attendance
		fields = ['roll_number', 'class_name', 'subject']

