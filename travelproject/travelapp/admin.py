from django.contrib import admin

from . models import Place
from . models import Quotes

# Register your models here.
admin.site.register(Place)
admin.site.register(Quotes)
