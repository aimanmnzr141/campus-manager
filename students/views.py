from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def add_student(request):
    return HttpResponse("Add Student Page")


def delete_student(request):
    return HttpResponse("Delete Student Page")
