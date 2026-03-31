from django.db import models
from Course.models import Course
from student_management.models import Student

# Create your models here.


#Table name EXAM

class Exam(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    exam_date = models.DateField()

    def __str__(self):
        return self.name
    


 #Table name Result

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.FloatField()
    
    @property
    def percentage(self):
        if self.total_marks > 0:
            return(self.marks_obtained/self.total_marks)*100


