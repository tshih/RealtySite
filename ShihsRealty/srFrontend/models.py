from django.db import models

# Create your models here.

class WebPage(models.Model):
	page_Name = models.CharField(max_length=200)
	page_Description = models.CharField(max_length=500)
	def __str__(self):
		return self.page_Name

class WebTextField(models.Model):
	text_Field_Name = models.CharField(max_length=200, default='index')
	text = models.TextField()
	pub_date = models.DateTimeField('date published')
	web_Page = models.ForeignKey(WebPage, on_delete=models.CASCADE)
	def __str__(self):
		return self.text_Field_Name