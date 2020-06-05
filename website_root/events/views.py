from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from .models import Student

def student_list(request):
    t = loader.get_template("student_list.html")
    studentList = Student.objects.all()
    # teacher = Student.teacher.name
    c = Context({"studentlist: ": studentList})
    return HttpResponse(t.render(c))
