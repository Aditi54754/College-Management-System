from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ROLE_CHOICE = (
        ('student','Student'),
        ('faculty','Faculty'),
        ('admin','Admin')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICE)

    def __str__(self):
        return self.user.username
    
