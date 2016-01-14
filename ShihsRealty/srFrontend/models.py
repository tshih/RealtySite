from django.db import models

# Create your models here.
class TextField(models.Model):
	question_text = models.TextField()
	pub_date = models.DateTimeField('date published')