from django.urls import path
from . import views
urlpatterns = [

    path('', views.homepage),
    path('hey1/',views.name, name='hey')
]
