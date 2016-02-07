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
	pub_Date = models.DateTimeField('date published')
	web_Page = models.ManyToManyField(WebPage)
	def __str__(self):
		return self.text_Field_Name

class Image(models.Model):
	BACKGROUND = 0
	CAROUSEL = 1
	STANDARD = 2

	IMAGE_TYPE = (
		(BACKGROUND, 'Background'),
		(CAROUSEL, 'Carousel'),
		(STANDARD, 'Standard'),
		)

	image_Name = models.CharField(max_length=200)
	image_Path = models.CharField(max_length=256)
	image_Type = models.IntegerField(choices=IMAGE_TYPE)

	def __str__(self):
		return self.image_Name