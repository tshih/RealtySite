from django.contrib import admin

from .models import WebTextField
from .models import WebPage
from .models import Image
# Register your models here.

admin.site.register(WebTextField)
admin.site.register(WebPage)
admin.site.register(Image)