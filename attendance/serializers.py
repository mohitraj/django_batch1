from rest_framework import serializers
from .models import Student
'''
class AttSerializer(serializers.Serializer):
	stuid = serializers.IntegerField()
	stuname = serializers.CharField(max_length=70)
	stmail = serializers.EmailField(max_length=70)
	stupass = serializers.CharField(max_length=70)

	def create(self,validated_data):
		return Student.objects.create(**validated_data)

	def update(self,instance, validated_data):
		instance.stuname = validated_data.get('stuname')
		instance.stmail = validated_data.get('stmail')
		instance.stupass = validated_data.get('stupass')
		instance.save()
		return instance

'''
def email_valid(value):
	if not value.endswith('gmail.com'):
		raise serializers.ValidationError("Not valid gmail")

class AttSerializer(serializers.ModelSerializer):
	stmail = serializers.CharField(validators=[email_valid])
	class Meta:
		model = Student 
		fields = ['stuid', 'stuname','stmail', 'stupass']
	'''
	def validate_stuid(self, value): # Field level validation 
		if value <=100:   #51   TRUE
			raise serializers.ValidationError("No valid roll number")
		return value 

	def validate(self,data):   # object level validation
		stuid = data.get('stuid')
		stuname = data.get('stuname')
		#if stuid >=50 or len(stuname)<5:  # 51 True 
		if stuid >=50:
			raise serializers.ValidationError("roll number and class not valid")
		return data
	'''