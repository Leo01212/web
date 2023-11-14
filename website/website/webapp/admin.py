from django.contrib import admin
from .models import table
from .models import people
# Register your models here.
admin.site.register(table)

admin.site.register(people)