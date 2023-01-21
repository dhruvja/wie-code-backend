from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path("register", views.registerUser, name="register"),
    path('getdocuments/<pk>', views.getDocuments, name="getdocuments"),
    path('uploaddocuments', views.uploadDocuments, name="uploaddocuments"),
    path('analyzedocuments/<pk>', views.analyzeDocuments, name="analyzedocuments"),
    path("updatetrack", views.updateTrack, name="updatetrack"),
    path('gettracks', views.getTracks, name="gettracks"),
    path('getpersonaldocuments', views.getPersonalDocuments, name="getpersonaldocuments"),
    path('getqr', views.getQR, name="getqr")
]