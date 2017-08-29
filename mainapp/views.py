from django.shortcuts import render


# Create your views here.

from django.shortcuts import render, render_to_response
from mainapp.classes import personal_core


me = personal_core.ClPersonalInfo('', '')
me.init_defaults()

def mainpage(request):
    return render_to_response("index.html",
                              {'name': me.name,
                               'birthdate': me.date_of_birth,
                               'skills': me.skills,
                               'hobbies': me.hobbies})

def studypage(request):
    return render_to_response("study.html", {'studies': me.studies})

def workpage(request):
    return render_to_response("work.html", {'works': me.works})
