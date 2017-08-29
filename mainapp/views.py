from django.shortcuts import render


# Create your views here.

from django.shortcuts import render, render_to_response
from mainapp.classes import personal_core
from mainapp.models import Hobby
from mainapp.models import Skill


def mainpage(request):
    me = personal_core.CLPersonalInfo('','')
    me.init_defaults()
    return render_to_response("index.html",
                              {'name': me.name,
                               'birthdate': me.date_of_birth,
                               'skills': Skill.objects.All(),
                               'hobbies': Hobby.objects.All() })

def studypage(request):
    return render_to_response("study.html")

def workpage(request):
    return render_to_response("work.html")
