from django.db import models
from student_management.models import Student
from Course.models import Course


class Attendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)
    