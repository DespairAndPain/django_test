from django.contrib import admin

from .models import signUp, tasks
from .forms import signUpForm, tasks_form
# Register your models here.

class signUpAdmin(admin.ModelAdmin):
	model = signUp
	form = signUpForm	
	list_display = ['full_name','email',"timestamp"]


class tasks_admin(admin.ModelAdmin):
	model = tasks
	#form = tasks_form	
	list_display = ['task_name','task',"timestamp"]
			

admin.site.register(tasks, tasks_admin)
admin.site.register(signUp, signUpAdmin)