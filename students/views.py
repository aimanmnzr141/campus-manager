from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def student_list(request):
    # Go to student table and give me all students data
    students = Student.objects.all()

    return render(request, "student_list.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("student_list")

    else:
        form = StudentForm()
        return render(request, "add_student.html", {"form": form})


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {"form": form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect(student_list)
