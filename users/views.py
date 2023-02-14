from django.http import HttpRequest, HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from users.forms import Sign_up_form, Sign_in_form
from django.contrib.auth import authenticate, login, logout



def sign_in_f(request: HttpRequest):
    if request.method == 'POST':
        form = Sign_in_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_url = reverse_lazy('home')
                    return HttpResponseRedirect(redirect_url)
    else:
        form = Sign_in_form()
    return render(request, 'signin.html', {'form': form})


def sign_up_f(request: HttpRequest):
    if request.method == 'POST':
        form = Sign_up_form(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = reverse_lazy('sign_in')
            return HttpResponseRedirect(redirect_url)
    else:
        form = Sign_up_form()
    return render(request, 'signup.html', {'form': form})


def logout_f(request: HttpRequest)->HttpResponse:
    logout(request)
    redirect_url = reverse_lazy('home')
    return HttpResponseRedirect(redirect_url)