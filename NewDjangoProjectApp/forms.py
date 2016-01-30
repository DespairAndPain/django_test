from django import forms

from .models import signUp, tasks

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

class signUpForm(forms.ModelForm):
	class Meta:
		model = signUp
		fields = ["full_name", "email"]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		print(email)
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension == "com":
			raise forms.ValidationError("Please use a valid .COM email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name



class tasks_form(forms.ModelForm):

	class Meta:
		model = tasks
		fields = ['task_name','task']

	def clean_task(self):
		task = self.cleaned_data.get('task')
		if len(task) == 0:
			raise forms.ValidationError("Please write a task")
		return task

	def clean_task_name(self):
		task = self.cleaned_data.get('task_name')
		if len(task) == 0:
			raise forms.ValidationError("Please write a task name")
		return task