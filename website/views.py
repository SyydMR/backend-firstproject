from django.shortcuts import render, get_object_or_404

from website.models import Destination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home_view(request):

    # ------------------------------------- #
    dests = Destination.objects.filter(status=1)
    # ------------------------------------- #
    dests = Paginator(dests, 6)
    try:
        page_number = request.GET.get('page')
        dests = dests.get_page(page_number)

    except PageNotAnInteger:
        dests = dests.get_page(1)
    except EmptyPage:
        dests = dests.get_page(1)
    context = {'dests':dests}





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

def ticket_view(request, pid):
    dest = get_object_or_404(Destination, pk=pid, status=1)
    context = {'dest':dest}
    return render(request, 'ticket.html', context)

def login_view(request):
    return render(request, 'login.html')







