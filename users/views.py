from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import json
from users.forms import CreateUserForm

@csrf_exempt
def login(request):
    if request.is_ajax():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user     = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                msg = json.dumps({'status' : 'ok'})
            else:
                msg = json.dumps({'status' : 'error'})

            return HttpResponse(msg)
    else:
        raise Http404

@csrf_exempt
def signup(request):
    if request.is_ajax():
        if request.POST:
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                auth.login(request, user)
                msg = json.dumps({'status' : 'ok'})
            else:
                msg = json.dumps({'status' : 'error', 'errors' : form.errors})
            return HttpResponse(msg)

    else:
        raise Http404

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/showcase")