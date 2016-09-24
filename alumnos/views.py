from django.shortcuts import render, redirect
# Create your views here.
from django.http import Http404
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from alumnos.forms import LoginForm
from django.utils.datastructures import MultiValueDictKeyError


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/dash')
            else:
                pass
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})



def dash(request):
    pass