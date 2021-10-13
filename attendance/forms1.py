from django import forms
from .models import Student, Att
class StuForms(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Student
		fields= ['stuid', 'stuname', 'stmail', 'password']


class MarkAtt(forms.ModelForm):
	class Meta:
		model = Att
		fields = ['name']