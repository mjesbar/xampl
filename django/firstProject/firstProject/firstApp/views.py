from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from django.http import HttpRequest
from django.template import context
import json

# Create your views here
def app(request):
    return HttpResponse(b'<h2>Aye!, your firstProject Helloworld in Django!!!</h2>')



def index(request):
    return render(request, 'index.html')



def dynamicValue(request):
    context : dict = { 
        'name': 'Mjesbar',
        'age': 26,
        'nationality': 'Colombian'
    }
    return render(request, 'dynamicValue.html', context=context)



def textInput(request):
    return render(request, 'textInput.html')

def counter(request):
    text = request.POST['text']
    #text = request.GET['text'] # Also available,, set method="GET" at form html tag.
    words : int = len(text.split())
    return render(request, 'counter.html', {'words': words})



def staticPage(request):
    return render(request, 'staticPage.html')



def simpleLogin(request):
    return render(request, 'simpleLogin.html')

def logged(request):
    content = request.META
    query = request.POST.copy()
    query = query.dict()
    return render(request, 'logged.html', {'content': content['USER'], 'query': query})



def post(request):
    options = ['profile_one', 'profile_two', 'profile_three']
    context = {
        'options': options
    }
    return render(request, 'post.html', context)

def postOption(request, pk):
    context = {'dynamic_profile_option': pk}
    return render(request, 'postOption.html', context)


