from django import forms
from  django.core import validators
BIRTH_YEAR_CHOICES = [str(each) for each in range(1980,2022)]
class AttForm(forms.Form):
	#label = forms.FieldType()
	stuid = forms.IntegerField(label= "ROLL")
	stuname = forms.CharField(validators=[validators.MinLengthValidator(10)])
	stmail = forms.EmailField(max_length=70)
	stupass = forms.CharField(widget = forms.PasswordInput(), max_length=70)
	'''
	def clean_stuname(self):
		valname= self.cleaned_data['stuname']
		if len(valname)<=2:
			raise forms.ValidationError("Enter more than 2 letter")
		return valname
	'''

	'''
	text = forms.CharField(widget = forms.Textarea, max_length=70)
	birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	'''
	'''
	def clean(self):
		cleaned_data = super().clean()
		valname= self.cleaned_data['stuname']
		email1 = self.cleaned_data['stmail']
		if len(valname)<=2:
			raise forms.ValidationError("Enter more than 2 letter")
		if len(email1)<8:

			raise forms.ValidationError("Enter more than 2 letter")
	'''
	