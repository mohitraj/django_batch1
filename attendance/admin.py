from django.contrib import admin

from .models import Student

#admin.site.register(Student)

# Register your models here.
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
	list_display = ["id" , "stuid", "stuname" ,"stmail", "stupass"]
