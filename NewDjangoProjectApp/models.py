from django.db import models

# Create your models here.

class signUp(models.Model):
	full_name = models.CharField(max_length=120, blank=True,null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    #def __unicode__(self):
    #	return self.full_name\

class tasks(models.Model):
	task_name = models.CharField(max_length = 140, blank = True, null = True)
	task = models.TextField(null = True, blank = True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)