from django.urls import path
from . import views


# this array contain the url tree to navigate through the app.
urlpatterns = [
    path('index/', views.index, name='index'),
    path('app/', views.app, name='app'),
    path('dynamicValue/', views.dynamicValue, name='dynamicValue'),
    path('textInput/', views.textInput, name='textInput'),
        path('textInput/counter',views.counter, name='counter'),
    path('staticPage/', views.staticPage, name='staticPage'),
    path('simpleLogin/', views.simpleLogin, name='simpleLogin')
]

