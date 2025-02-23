from django.shortcuts import render
from main.crawling import crawling
# Create your views here.
from django.http import HttpResponse
from django.template import loader
import datetime

crawling_tmp = crawling()

def homeView(request):
    context = {
        'images': crawling_tmp[0],
        'urls': crawling_tmp[1],
        'status': crawling_tmp[2],
        'n': range(len(crawling_tmp[0])),
    }
    return render(request, 'home.html', context)

def teamView(request):
    return render(request,'team.html',None)

def joinView(request):
    return render(request,'join.html',None)

def editView(request):
    return render(request,'edit.html',None)

def loginView(request):
    return render(request,'login.html',None)

def logoutView(request):
    return render(request,'logout.html',None)

def qnaView(request):
    return render(request,'qna.html',None)

def guideView(request):
    return render(request,'guide.html',None)
