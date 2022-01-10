from django.urls import path
from .views import index

app_name = 'motorapp'

urlpatterns = [
    path("", index, name='index'),
]
