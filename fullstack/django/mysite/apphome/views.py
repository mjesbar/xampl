from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Return the homepage."""
    return render(request, 'home.html')
   

def room(request):
    """
    Return the room page."""
    #  return HttpResponse("Hello, world. room-url is working.")
    return render(request, 'room.html')


def variable(request):
    """
    Return the shared_variables page."""
    var = 'This is a variable : String'
    vars = ['var1', 'var2', 'varN', '. . .']
    context = {'data': var, 'datas': vars}
    return render(request, 'variable.html', context)


def extend(request):
    """
    Return the extend-html page."""
    return render(request, 'extend.html')



