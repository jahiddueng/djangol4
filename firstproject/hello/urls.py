from django.urls import path
from . import views
urlpatterns = [
        path("", views.index, name ="index"),
        path("jahid", views.jahid, name ="jahud"),
        path("farhana", views.farhana, name ="farhana"),
        path("<str:name>", views.greet, name ="greet")
    ]
