from django.contrib import admin

from .models import WebTextField
from .models import WebPage
# Register your models here.

admin.site.register(WebTextField)
admin.site.register(WebPage)