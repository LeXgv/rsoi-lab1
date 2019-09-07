from django.db import models

class Person(models.Model):
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    patronymic = models.CharField(max_length=50)
    old = models.IntegerField()

class Work(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    pay = models.IntegerField()
