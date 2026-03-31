from django.db import models
from student_management.models import Student


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration_year = models.IntegerField()


    def __str__(self):
        return self.name
        


class Subject(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Credits = models.IntegerField()


    def __str__(self):
        return self.name                                                               
        



# TABLE ENROLLMENT

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.IntegerField()
    session = models.CharField(max_length=50)

    def __str__(self):
        return self.session
    

