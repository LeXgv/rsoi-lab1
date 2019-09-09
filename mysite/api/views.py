from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import forms
from django import forms
from django.core.exceptions import *
import django.db.models
import json

class Api_JsonResponseGetError(HttpResponse):
    def __init__(self, _id, _type):
        HttpResponse.__init__(self, '{"type": "error", "id": %d, "info": "%s"}' % (_id, _type), content_type = "text/json")

def models_to_json(_models):
    if not isinstance(_models, (list, django.db.models.query.QuerySet)):
        _models = [_models]
    if len(_models) == 0:
        return '[]'
    json_list = '['
    for el in _models:
        if isinstance(el, django.db.models.Model):
            json_list += el.to_json()+','
        else:
            raise ValueError("list contain not object type django.db.model.Models. Now type is " + str(type(el)))
    json_list = json_list[:-1]
    json_list += ']'
    return json_list

def get_form_users(request, case):
    if request.method == 'GET':
        if request.GET == {}:
            if case == 'get':
                bt = "Получить пользователя"
                provide = 'get'
            elif case == 'add':
                bt = "Добавить пользователя"
                provide = "add"
            add_form = forms.addPerson()
            return render(request, 'api/form.html', {'form': add_form, 'button_title': bt, 'provide': provide})
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed("GET")

'''--=====API=====--'''
@csrf_exempt
def users(request):
    print(request.GET)
    if request.method == 'GET':
        if request.GET == {}:
            persons = models.Person.objects.all()
            return HttpResponse(models_to_json(persons), content_type='text/json')
        else:
            if len(request.GET) != 1:
                return Api_JsonResponseGetError(1, "You sent in request type get more then one argument")
            try:
                if list(request.GET.keys())[0] == 'id':
                    persons = models.Person.objects.get(pk = request.GET['id'])
                elif list(request.GET.keys())[0] == 'name':
                    persons = models.Person.objects.get(name=request.GET['name'])
                else:
                    return Api_JsonResponseGetError(3, 'wrong argument')
            except ObjectDoesNotExist:
                return Api_JsonResponseGetError(2, "Object does not exist")
            return HttpResponse(models_to_json(persons), content_type='text/json')
    elif request.method == "POST":
        print("======")
        print(str(request.body))
        print(type(request.body))
        print("======")
        data = json.loads(request.body)
        if not isinstance(data, list):
            data = [data]
        for el in data:
            if not models.RequestChecker_addPerson(el).is_valid():
                return Api_JsonResponseGetError(4, "Wrong json object.")
        for el in data:
            models.Person(**el).save()
    return HttpResponse('ok', content_type='text/json')

@csrf_exempt
def clear_base(request):
    if request.method == "GET":
        try:
            print(request.GET['key'])
            if request.GET['key'] == '123':
                for el in models.Person.objects.all():
                    el.delete()
            else:
                return HttpResponse('Wrong Key')
        except KeyError:
            return HttpResponse('KeyError')
    return HttpResponse('ok')
