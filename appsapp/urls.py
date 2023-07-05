from django.urls import path

from appsapp import views

urlpatterns=[
    path('',views.appli_form,name="appli_form")
]