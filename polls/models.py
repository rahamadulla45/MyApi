from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	image = models.ImageField(null=True, blank=True)
	owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)




	def __str__(self):
		return self.first_name