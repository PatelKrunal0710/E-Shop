from django.shortcuts import render, redirect
from .forms import createUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import product

def registerPage(request):
    form = createUserForm()
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})

def loginPage(request):
    if request.method=="POST":
        print("POST Request sent")
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['userid'] = request.user.id
            request.session['email'] = request.user.email
            return redirect('index')
        else:
            return render(request, 'users/login.html', {'error':'username or password is incorrect'})
    return render(request, 'users/login.html')

def logout(request):
    request.session.clear()
    return redirect('login')