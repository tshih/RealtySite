from django.db import models

# Create your models here.
class WebTextField(models.Model):
	question_text = models.TextField()
	pub_date = models.DateTimeField('date published')

#class WebPage(models.Model):
