from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.redirect),
    path('/', views.index),
    path('/users', views.create_user),
    path('/success', views.success)
]