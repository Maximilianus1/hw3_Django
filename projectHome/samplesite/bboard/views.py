from django.shortcuts import render
from django.http import  HttpResponse
from .models import Bb,Rubric
from django.template import loader
from .forms import BbForm,RubricForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def index(request):

    bbs = Bb.objects.all()
    rubrics =Rubric.objects.all()
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def login(request):
    return render(request, 'bboard/login.html')
