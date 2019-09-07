from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse
from . import models
# Create your views here.
from . import models
from . import forms
from django.views.decorators.http import require_http_methods


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
        return HttpResponseNotAllowed("GET")

#API
def users(request):
    return HttpResponse('ОК!');