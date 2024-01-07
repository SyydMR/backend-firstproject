from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('website:home'))


        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'login.html', context)
    else:
        return redirect('/home')






@login_required
def logout_view(request):
    logout(request)
    return redirect('/home')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form.save()
        return reverse('accounts:login')

            




    form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'signup.html', context)




