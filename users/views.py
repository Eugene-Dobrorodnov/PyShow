from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from users.forms import CreateUserForm

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/showcase")
        else:
            return HttpResponseRedirect("/account/error/")
    else:
        return render(request, 'users/login_form.html', '')

def signup(request):
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
            auth.login(request, user)
            return HttpResponseRedirect("/showcase")
        else:
            return render(request, 'users/signup_form.html', {'form':form})
    else:
        context =  {'form' : CreateUserForm}
        return render(request, 'users/signup_form.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/showcase")