from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice


# Create your views here.

def home(request):
    """
    Return the homepage.
    """
    return render(request, 'apphome/home.html')
  


def room(request):
    """
    Return the room page.
    """
    return render(request, 'apphome/room.html')



def variable(request):
    """
    Return the shared_variables page.
    """
    var = 'This is a variable "var": String'
    vars = ['var1', 'var2', 'varN', '. . .']
    context = {'data': var, 'datas': vars}

    return render(request, 'apphome/variable.html', context)
 


def extend(request):
    """
    Return the extend-html page.
    """
    template = loader.get_template("apphome/extend.html")
    return HttpResponse(template.render(request=request))



def view(request, question_id):
    """
    Return the view question-request page.
    """
    # try: question = Question.objects.get(id=question_id)
    # except: raise Http404("This Fucked page doesn't charge")

    question = get_object_or_404(Question, pk=question_id)

    response = "Hello, world. view-url is working. Question ID: %s.<br> Question Text: <h2>%s</h2>."\
        % (question_id, question.question_text)

    return HttpResponse(response)













