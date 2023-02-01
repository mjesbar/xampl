from django.urls import path
from django.urls.conf import _path
from . import views


# this array contain the url tree to navigate through the app.
urlpatterns = [
    path('', views.index, name='index'),
    # basic app
    path('app/', views.app, name='app'),
    # inserting value with from python varibales
    path('dynamicValue/', views.dynamicValue, name='dynamicValue'),
    # text catching through textinput tag, and counter backend
    path('textInput/', views.textInput, name='textInput'),
        path('textInput/counter',views.counter, name='counter'),
    # Page loading static resources
    path('staticPage/', views.staticPage, name='staticPage'),
    # login example
    path('simpleLogin/', views.simpleLogin, name='simpleLogin'),
        path('simpleLogin/logged', views.logged, name='logged'),
    # Dinamic Urls
    path('post/', views.post, name='post'),
        path('post/<str:pk>', views.postOption, name='postOption')
]

