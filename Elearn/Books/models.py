from django.db import models
from django.contrib.auth.models import User
from Courses import models as Courses_Model

class Books(models.Model):
	name=models.CharField(max_length=200)
	file=models.FileField(null=True,upload_to='')
	courses=models.CharField(max_length=200,default=' ')
	uploaded_by=models.CharField(max_length=200)
	is_approved=models.BooleanField(default='False')

	class Meta:
		verbose_name_plural='Books'

	def __str__(self):
		return self.name		
