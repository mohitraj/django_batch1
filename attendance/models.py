from django.db import models

class Student(models.Model):
	stuid = models.IntegerField()
	stuname = models.CharField(max_length=70)
	stmail = models.EmailField(max_length=70)
	stupass = models.CharField(max_length=70)


	def __str__(self):
		return str(self.stuid)

class Att(models.Model):
	name =  models.CharField(max_length=70)
	time = models.IntegerField()


class Master_data(models.Model):
	class Meta:
		unique_together = (('roll_number', 'class_name'),)
		
	roll_number = models.IntegerField("Roll Number", null=False)
	name = models.CharField("Name", max_length = 120, null=False)
	email = models.EmailField('Email', null=False)
	class_name = models.CharField("Class Name", max_length=20,null=False)

	def __str__(self):
			return str(self.name)

class Mark_Attendance(models.Model):
	class meta:
		unique_together = (('roll_number','date1'),)
		unique_together = (("date1", 'ip_address'),)
	roll_number = models.IntegerField("Roll Number", null=False)
	class_name = models.CharField("Class Name", max_length=20,null=False)
	subject  = models.CharField('Subject', max_length=100, null=False)
	time1 = models.IntegerField(null=False)
	ip_address = models.CharField(max_length=100, null=False)
	date1 = models.CharField(max_length=100, null=False)
	platform = models.CharField(max_length=200, null=False)
	Master1 = models.ForeignKey('Master_data', related_name= 'roll_no', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.roll_number)

class Mark_Attendance3(models.Model):
	class meta:
		#unique_together = (('roll_number','date1'),('date1', 'ip_address'))
		constraints = [
            models.UniqueConstraint(fields=['roll_number','date1'], name='no_duplicate_att'),
            models.UniqueConstraint(fields=['date1', 'ip_address'], name='no_proxy')
    ]
	roll_number = models.IntegerField("Roll Number", null=False)
	class_name = models.CharField("Class Name", max_length=20,null=False)
	subject  = models.CharField('Subject', max_length=100, null=False)
	time1 = models.IntegerField(null=False)
	ip_address = models.CharField(max_length=100, null=False)
	date1 = models.CharField(max_length=100, null=False)
	platform = models.CharField(max_length=200, null=False)
	Master1 = models.ForeignKey('Master_data', related_name= 'roll_no1', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.roll_number)

class Mark_Attendance4(models.Model):
	class meta:
		#unique_together = (('roll_number','date1'),('date1', 'ip_address'))
		constraints = [
            models.UniqueConstraint(fields=['roll_number','date1'], name='no_duplicate_att'),
            models.UniqueConstraint(fields=['date1', 'ip_address'], name='no_proxy')
    ]
	roll_number = models.IntegerField("Roll Number", null=False)
	class_name = models.CharField("Class Name", max_length=20,null=False)
	subject  = models.CharField('Subject', max_length=100, null=False)
	time1 = models.IntegerField(null=False)
	ip_address = models.CharField(max_length=100, null=False)
	date1 = models.CharField(max_length=100, null=False)
	platform = models.CharField(max_length=200, null=False)
	Master1 = models.ForeignKey('Master_data', related_name= 'roll_no2', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.roll_number)






