from django.urls import path
from . import views
urlpatterns = [
    path("", views.Home_Page),
    path("newview", views.New)
]