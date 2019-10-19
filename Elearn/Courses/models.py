from django.db import models
from django.contrib.auth.models import User
#from Clubs import models as Clubs_Model

class Shared_notes(models.Model):
	name=models.CharField(max_length=200)
	uploaded_by=models.CharField(max_length=200)
	uploaded_at=models.DateTimeField(auto_now_add=True)

class Videos(models.Model):
	name=models.CharField(max_length=200)
	uploaded_by=models.CharField(max_length=200)
	uploaded_at=models.DateTimeField(auto_now_add=True)	
	videos=models.FileField()


class CoursesC(models.Model):
	name=models.CharField(max_length=200)
	shared_notes=models.ManyToManyField(Shared_notes,related_name='courses')
	videos=models.ForeignKey(Videos,related_name='courses',on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural='Courses for Clubs and Departments'



class CoursesE(models.Model):
	name=models.CharField(max_length=200)
	link=models.CharField(max_length=500,null=True)
	is_recommended=models.BooleanField(default=False)
	uploaded_by=models.CharField(max_length=200)
	class Meta:
		verbose_name_plural='External Courses'


	def __str__(self):
		return self.name