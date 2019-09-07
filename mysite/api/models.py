from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField()

    @classmethod
    def findByName(cls, name):
        return cls.objects.get(name=name)


