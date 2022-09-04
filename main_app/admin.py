from django.contrib import admin

# Register your models here.
from . models import Media
from . models import Journal

admin.site.register(Media)
admin.site.register(Journal)