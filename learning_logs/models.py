from django.db import models
from django.contrib.auth.models import User 

#we will need to create models such as class to tell Django how to work 
#with the data we will be providing .
#Our users need to create a topic they are learning and we will need to keep 
#time stamp of each learning logs .

class Topic(models.Model):
	"""A topic the user is learning about """
	text= models.CharField(max_length=200)
	date_added= models.DateTimeField(auto_now_add=True)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string version of the model or our class"""
		return self.text


class Entry(models.Model):
	"""what the user learned about a topic"""
	topic= models.ForeignKey(Topic,on_delete=models.CASCADE)
	text= models.TextField()
	date_added= models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural="entries"

	def __str__(self):
		"""return a string """

		if len(self.text) > 50:
			return self.text[:50] + "...."
		else:
			return  self.text
