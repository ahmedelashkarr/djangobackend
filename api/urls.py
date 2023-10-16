from django.urls import path
from .views import api, api_details
urlpatterns = [
    path('', api.as_view()),
    path('<str:slug>', api_details),
]
