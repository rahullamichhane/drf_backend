from django.db import models


class ClassCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):  
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    address = models.TextField()
    class_category = models.ForeignKey(ClassCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.student_id})"


# Create your models here.
