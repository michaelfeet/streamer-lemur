from django.contrib import admin

# Register your models here.
from . models import Media
from . models import Journal
from . models import Photo

admin.site.register(Media)
admin.site.register(Journal)
admin.site.register(Photo)