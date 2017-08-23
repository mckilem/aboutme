from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response


def mainpage(request):
    return render_to_response("index.html")


def studypage(request):
    return render_to_response("study.html")


def workpage(request):
    return render_to_response("work.html")
