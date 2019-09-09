from django.db import models
from django import forms
import json

class Person(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)

    @classmethod
    def findByName(cls, name):
        return cls.objects.get(name=name)

    def to_json(self):
        return json.dumps({"type": 'dbPerson', 'id': self.pk, 'name': self.name, 'age': self.age})

class RequestChecker_addPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']

