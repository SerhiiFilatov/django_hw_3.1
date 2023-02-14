
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from tasks.models import *
from tasks.forms import *
import uuid

def homepage(request: HttpRequest)->HttpResponse:
    return render(request, 'homepage.html')


def task_detail(request: HttpRequest, slug)->HttpResponse:
    try:
        ctx = {'object_slug': tasks.objects.get(slug=p_slug)}
    except Post.DoesNotExist:
        raise Http404('not found')
    return render(request, 'task_detail.html', ctx)


def task_create_form(request: HttpRequest)->HttpResponse:
    if request.method == 'POST':
        form = Task_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.reporter = request.user
            instance.save()
            redirect_url = reverse_lazy('task_det', kwargs={'pk':instance.pk})
            return HttpResponseRedirect(redirect_url)
    else:
        form = Task_form()
    return render(request, 'task_form.html', {'form': form})


def task_update_form(request: HttpRequest)->HttpResponse:
    try:
        instance = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        raise Http404('task not found')
    if request.method == 'POST':
        form = Task_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = Task_form(instance=instance)
    return render(request, 'task_form.html', {'form': form})
