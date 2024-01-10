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
            next = request.POST.get('next')
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)
                print(user is None)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Logged in successfully as {user.username}!")
                    return redirect(next)
            else:
                messages.error(request, "Wrong credentials!")
                return redirect(reverse('accounts:login'))

        form = AuthenticationForm()
        if request.GET.get('next'):
            next = request.GET.get('next')
        else:
            next = reverse('accounts:login')
        context = {'form':form, 'next':next}
        return render(request, 'login.html', context)
    else:
        return redirect('/home')






@login_required
def logout_view(request):
    logout(request)
    return redirect('/home')



def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.national_code = request.POST["national_code"]
                user.phone = request.POST["phone"]
                user.save()
                login(request, user)
                messages.success(request, "Signed up successfully!")
                return redirect('/home')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
                        return redirect(reverse('accounts:signup'))

        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    
    else:
        return redirect('/home')

