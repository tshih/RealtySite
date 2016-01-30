from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import WebTextField
from .models import WebPage

# Create your views here.
def index(request):

	indexTextFields = dict(WebTextField.objects.filter(web_Page__page_Name="Index").values_list('text_Field_Name', 'text'))
	return render(request, 'srFrontend/index.html',indexTextFields)
