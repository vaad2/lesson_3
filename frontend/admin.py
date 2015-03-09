from django.contrib import admin
from .models import Template
# Register your models here.

admin.site.register(Template, list_display=['id', 'name', 'status'], list_editable=['name', 'status'])

