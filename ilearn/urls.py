from django.urls import path
from . import views

urlpatterns = [
    path('git ', views.index, name="index")
]