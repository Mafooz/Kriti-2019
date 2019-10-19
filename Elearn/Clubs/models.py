from django.db import models
from django.contrib.auth.models import User
from Courses import models as CM


class Clubs(models.Model):
	name=models.CharField(max_length=200,unique=True)
	courses=models.ManyToManyField(CM.CoursesC,related_name='clubs')
	CLUB = 'CL'
	DEPARTMENT = 'DE'
	EXTERNAL = 'EX'
	CHOICE_OF_SOURCES = [
		(CLUB, 'CL'),
		(DEPARTMENT, 'DE'),
		(EXTERNAL, 'EX'),
	]
	source=models.CharField(max_length=2,choices=CHOICE_OF_SOURCES,default=CLUB)

