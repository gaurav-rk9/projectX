from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('sample/',views.sample,name="sample"),
    path('listing/',views.listing,name="listing"),
    path("",views.home,name="home"),
    path("<int:question_id>",views.question,name="question")
]