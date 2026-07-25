from django.contrib import admin

# "."->(current package) in models here indicate that both admin and models are in the same students app
from .models import Student

# Register your models here.
admin.site.register(Student)
