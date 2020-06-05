from django.db import models

from django.db import models

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    class Meta:
        db_table = 'teacher'

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', max_length=50)
    age = models.IntegerField()
    intime = models.DateField()
    gender = models.IntegerField(max_length = 60)
    # teacher = models.ForeignKey(Teacher, related_name='tutor')
    class Meta:
        db_table = 'student'