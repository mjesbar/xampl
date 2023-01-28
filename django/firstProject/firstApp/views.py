from django.shortcuts import render
from django.http import HttpResponse
from django.template import context

# Create your views here
def app(request):
    return HttpResponse('<h2>Aye!, your firstProject Helloworld in Django!!!</h2>')



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
