from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

def home(request):
    """Return the homepage."""
    return render(request, 'apphome/home.html')
#endef


def room(request):
    """Return the room page."""
    return render(request, 'apphome/room.html')
#endef


def variable(request):
    """Return the shared_variables page."""
    request_headers = [request.headers, request.body, request.path, request.method, request.scheme, type(request.POST)]
    varn = ['var1', 'var2', 'varN', '. . .']
    context = {'data': request_headers, 'datas': varn}

    return render(request, 'apphome/variable.html', context)
#endef


def extend(request):
    """Return the extend-html page."""
    template = loader.get_template("apphome/extend.html")

    return HttpResponse(template.render(request=request))
#endef


def view(request, question_id):
    """Return the view question-request page."""
    question = get_object_or_404(Question, pk=question_id)
    question_list = Question.objects.all()
    print(question, request.POST, request.method)
    if (request.method == "GET"):
        # Case page refreshed or something else of the normal POST form sending, so
        # Prints the view with the default question enquire.
        question_default = get_object_or_404(Question, pk=1)
        print("Question default: ", question_default.question_text)
        return render(request, "apphome/view.html", {"question": question_default, "question_list": question_list, "question_selected": question_default})
    elif (request.method == "POST"):
        # Prints view with the question selected.
        question_item = request.POST.get("question") if request.POST.get("question") else 1
        question_selected = Question.objects.get(pk=question_item)
        question_selected.visits += 1
        question_selected.save()
        context = {
            "question": question,
            "question_list": question_list,
            "question_selected": question_selected
        }
        #  return render(request, "apphome/view.html", context)
        return HttpResponseRedirect("/apphome/room/")
#endef


def static(request):
    """Return a static linked page."""
    return render(request, 'apphome/static.html')
#endef


