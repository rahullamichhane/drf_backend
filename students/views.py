from django.shortcuts import render
from .models import Student  # only if you want to use the Student model

def student_list(request):
    students = Student.objects.all()  # optional if you want to display data
    return render(request, 'students/simple_student_list.html', {'students': students})


