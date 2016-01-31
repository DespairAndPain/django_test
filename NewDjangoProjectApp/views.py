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
    
	if request.method == 'POST':
		print(request.POST)

	form = tasks_form(request.POST)
	if request.user.is_authenticated():

		qeury = tasks.objects.all()
		#if len(request.POST) > 0:
		_task = form.cleaned_data.get('task')
		_task_name = form.cleaned_data.get('task_name')
		
		tasks_model = tasks(task_name=_task_name, task=_task,user=request.user)
		tasks_model.save()
		
			

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