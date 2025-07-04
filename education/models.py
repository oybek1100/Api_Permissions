from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    is_premium_user = models.BooleanField(default=False)

class Subject(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='subjects', null=True, blank=True)

    def __str__(self):
        return self.name 

class Course(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField(null=True, blank=True)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    owner = models.ForeignKey(
        CustomUser,
        related_name='owners',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='course/images')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    is_premium = models.BooleanField(default= False)

