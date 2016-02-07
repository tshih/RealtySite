from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import WebTextField
from .models import WebPage

# Create your views here.
def index(request):

	indexTextFields = dict(WebTextField.objects.filter(web_Page__page_Name="Index").values_list('text_Field_Name', 'text'))
	return render(request, 'srFrontend/index.html',indexTextFields)

def about(request):
	aboutTextFields = dict(WebTextField.objects.filter(web_Page__page_Name="About").values_list('text_Field_Name', 'text'))
	return render(request, 'srFrontend/about.html', aboutTextFields)

# def blog(request):
# 	blogTextFields = dict(WebTextField.objects.filter(web_Page__page_Name="Blog").values_list('text_Field_Name', 'text'))
# 	return render(request, 'srFrontend/blog.html', blogTextFields)

def contact(request):
	contactTextFields = dict(WebTextField.objects.filter(web_Page__page_Name="Contact").values_list('text_Field_Name', 'text'))
	return render(request, 'srFrontend/contact.html', contactTextFields)	
