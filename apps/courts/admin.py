from django.contrib import admin

# Register your models here.
from .models import Court, SelectedCourt

admin.site.register(Court)
admin.site.register(SelectedCourt)