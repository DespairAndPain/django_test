from django.shortcuts import render
from .forms import signUpForm
from .models import signUp
# Create your views here.

def home(request):

	form = signUpForm(request.POST or None)

	context = {
			"title": "Register now",
			"form": form
		}

	if form.is_valid():
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")

		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()

		context = {
			"title": "Thank you"
		}

	return render(request, "home.html",context)

def profile(request):
    
	if request.user.is_authenticated() and request.user.is_staff:

		qeury = signUp.objects.all();

		context = {
				"title": "Register now",
				"queryset": qeury
			}

	

	return render(request, "profile.html",context)