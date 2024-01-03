from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# def http_test(requests):
#     return HttpResponse('hello world')

# def json_test(requests):
#     return JsonResponse({'hello world':'3'})
from website.models import Destination


def home_view(request):
    # ------------------------------------- #
    dests = Destination.objects.filter(status=1)
    context = {'dests':dests}
    # ------------------------------------- #
    return render(request, 'home.html', context)

def aboutus_view(request):
    return render(request, 'aboutus.html')

def factor_view(request):
    return render(request, 'factor.html')

def panel_view(request):
    return render(request, 'panel.html')

def questions_view(request):
    return render(request, 'questions.html')

def signup_view(request):
    return render(request, 'signup.html')

def ticket_view(request):
    return render(request, 'ticket.html')

def login_view(request):
    return render(request, 'login.html')







