from django.db import models

# Create your models here.
# This student model will represent the structure of student table in db
class student(models.Model):
    # Stores the student's full name 
    name = models.CharField(max_length=100)
    # Stores the unique roll no of student
    roll_number = models.CharField(max_length=20 , unique=True)
    # Stores unique email address of student
    email = models.EmailField(unique=True)
    # Stores course name of student
    course = models.CharField(max_length=100)
    # Stores the age of student (only positive value)
    age = models.PositiveIntegerField()

# This function will return the string representation of student object
    def __str__(self):
    return self.name
