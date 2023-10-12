from django.urls import path 
from . import views
from knox import views as knox_views
urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    

]
