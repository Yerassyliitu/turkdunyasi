from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models




class Client_forms(models.Model):
    name = models.CharField(max_length=30)
    number = PhoneNumberField(unique=True)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    school_class = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, null=True, blank=True)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name



class University(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    structure = models.TextField(null=True, blank=True)
    rating = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100)
    price = models.IntegerField()
    program = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default=" ")


    def __str__(self):
        return self.title


class Faculty(models.Model):
    faculty = models.CharField(max_length=200)
    university = models.ForeignKey(University, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty


class Image_src(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    image_scr = models.TextField(default='images/1_first.png')
    first = models.BooleanField(default=True)
    second = models.BooleanField(default=True)


class MyModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)




''
