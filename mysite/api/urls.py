from django.urls import path
from . import views

urlpatterns = [
    path('forms/users/<str:case>', views.get_form_users),
    path('v1/users/', views.users),
    path('v1/clear_db/', views.clear_base),
   # path('v1/work/', views.work),
]