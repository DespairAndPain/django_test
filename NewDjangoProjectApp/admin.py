from django.contrib import admin

from .models import signUp
from .forms import signUpForm
# Register your models here.

class signUpAdmin(admin.ModelAdmin):
	model = signUp
	form = signUpForm	
	list_display = ['full_name','email',"timestamp"]
		
		

admin.site.register(signUp, signUpAdmin)