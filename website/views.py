from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from website.models import Destination, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.models import Invoice, NationalCodes, Destination_City
from website.forms import CommentForm, PanelForm
from django.contrib import messages

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
        for i in range(count):
            base_str = 'national_code_'
            national_code_number = base_str + str(i + 1)
            national_code_list.append(national_code_number)
        return national_code_list

    if request.method == 'POST':
        name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        origin = request.POST.get('oigin_name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        count_national_code = request.POST.get('count_ncode')
        national_codes = request.POST.get('national_code_')
        ncode_list_name = national_code_creator(count_national_code)
        ncode_list_value = []
        for ncode in ncode_list_name:
            ncode_list_value.append(request.POST.get(ncode))
        
        









        new_Inv = Invoice()
        new_NationalCode = NationalCodes()

    origin_cities = Destination_City.objects.filter(destination_id=pid)
    dest = get_object_or_404(Destination, pk=pid, status=1)
    context = {'dest':dest, 'origin':origin_cities}
    return render(request, 'ticket.html', context)


















