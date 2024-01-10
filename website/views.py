from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from website.models import Destination, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.models import *
from website.forms import CommentForm, PanelForm, TicketForm
from django.contrib import messages
from accounts.models import User
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

@login_required
def panel_view(request):

    if request.method == 'POST':
        user_form = PanelForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
        else:
            messages.error(request, 'Something went wrong!')

    else:
        user_form = PanelForm(instance=request.user)


    return render(request, 'panel.html', {'user_form': user_form})




@login_required
def questions_view(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your comment submited successfully !")
        else:
            messages.error(request, f"Something went wrong!")

    comments = Comment.objects.filter(approved=True).order_by('created_date')
    form = CommentForm()
    context = {'comments':comments, 'form':form}
    return render(request, 'questions.html', context)


def ticket_view(request, pid):
    
    def national_code_creator(count):
        national_code_list = []
        if (count == None) or (count == ''):
            count = 0
        for i in range(int(count)):
            base_str = 'national_code_'
            national_code_number = base_str + str(i + 1)
            national_code_list.append(national_code_number)
        return national_code_list
    
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            count_national_code = request.POST.get('count_ncode')
            if (count_national_code != None) and (count_national_code != '') and (count_national_code != 0):
                ncode_list_name = national_code_creator(count_national_code)
                ncode_list_value = []

                for ncode in ncode_list_name:
                    ncode_list_value.append(request.POST.get(ncode))

                origin_city = request.POST.get('origin-city')
                tab = request.POST.get('tabs')

                






                
            
                form = TicketForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.save()
                    messages.success(request, "Signed up successfully!")

                    form = TicketForm()
                    context = {'form': form}
                    return redirect(request, 'factor.html', context)




                trans = Transportation()
                city = get_object_or_404(City, pk=origin_city)
                nncodes = NationalCodes()
                user = User()
                origin_cities = Destination_City.objects.filter(destination_id=pid)
                dest = get_object_or_404(Destination, pk=pid, status=1)
                context = {'dest':dest, 'origin':origin_cities, 'trans': trans, 'nncodes': nncodes, 'user':user, 'city':city}

                return render(request, 'factor.html', context)
        

    origin_cities = Destination_City.objects.filter(destination_id=pid)
    dest = get_object_or_404(Destination, pk=pid, status=1)
    context = {'dest':dest, 'origin':origin_cities}

    return render(request, 'ticket.html', context)


















