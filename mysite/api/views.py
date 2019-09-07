from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.
from . import models
from . import forms
#from django.views.decorators.http import require_http_methods
from django import forms
from django.core.serializers import serialize
from django.core.exceptions import *
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

#API
@csrf_exempt
def users(request):
    print("==========================")
    print(request.method)
    print("==========================")
    if request.method == 'GET':
        if request.GET == {}:
            persons = models.Person.objects.all()
            return HttpResponse(serialize('json', persons), content_type='text/json')
        else:
            if len(request.GET) != 1:
                return HttpResponseBadRequest()
            try:
                if list(request.GET.keys())[0] == 'id':
                    persons = models.Person.objects.get(pk = request.GET['id'])
                elif list(request.GET.keys())[0] == 'name':
                    persons = models.Person.objects.get(name=request.GET['name'])
                if not isinstance(persons, list):
                    persons = [persons]
            except ObjectDoesNotExist:
                return HttpResponse('', content_type='text/json')

            return HttpResponse(serialize('json', persons), content_type='text/json')
    elif request.method == "POST":
        print(request.GET)
        print('---------')
        print(request.body)
   # return HttpResponseNotAllowed()
    return HttpResponse('', content_type='text/json')

