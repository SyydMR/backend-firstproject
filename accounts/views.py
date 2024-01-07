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
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            

            user.save()
            messages.success(request, "Signed up successfully!")
            return redirect('accounts:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


