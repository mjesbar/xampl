from django.urls import path

from . import views

app_name = "apphome"
urlpatterns = [
    path("", views.home, name="home"),
    path("room/", views.room, name="room"),
    path("variable/", views.variable, name="variable"),
    path("extend/", views.extend, name="extend"),
    path("view/<int:question_id>/", views.view, name="view"),
    path("static/", views.static, name="static")
]
