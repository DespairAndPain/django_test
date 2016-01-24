from django import forms

from .models import signUp

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