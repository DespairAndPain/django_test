from django.shortcuts import render
from .forms import signUpForm, tasks_form
from .models import signUp,  tasks
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
    
	form = tasks_form(request.POST)
	if request.user.is_authenticated():

		qeury = tasks.objects.all()
		print(request.POST)
		#if len(request.POST) > 0:

			#instance = form.save(commit=False)
			#instance.save()
			

		context = {
				"title": "Register now",
				"queryset": qeury,
				'form': form,
			}

	else:
		context = {
				'title': "You'r not prepare",
				'form': form,
			}

	return render(request, "profile.html", context)