from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    template = loader.get_template('polls/detail.html')
    print(question)
    return HttpResponse(template.render({'question': question}, request))

def results(request, question_id):
    return HttpResponse("You're looking at the result of question %s." % question_id)

def json_example(request):
    response = {"User":
                    {"fname": "Vasya",
                     "lname": "Ivanov",
                     "age": 25},
                "Permission":
                    {'SQL': "All",
                     "Server": "All"}
                }
    return JsonResponse(response)