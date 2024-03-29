from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("/<int:question_id>/", views.detail, name='detail'),
    path("/<int:question_id>/results/", views.results, name="results"),
    #path("/<int:question_id>/vote/", views.vote, name="vote"),
    path("/json/", views.json_example, name = 'json_example')
]