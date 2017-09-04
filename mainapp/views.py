from django.shortcuts import render


# Create your views here.

from django.shortcuts import render, render_to_response
from mainapp.classes import personal_core
from mainapp.models import Skill
from mainapp.models import Work
from mainapp.models import Study
from mainapp.models import Hobby


me = personal_core.ClPersonalInfo('', '')
me.init_defaults()

def mainpage(request):
    return render_to_response("index.html",
                              {'name': me.name,
                               'birthdate': me.date_of_birth,
                               'skills': Skill.objects.all(),
                               'hobbies': Hobby.objects.all()})

def studypage(request):
    return render_to_response("study.html", {'studies': Study.objects.all()})

def workpage(request):
    return render_to_response("work.html", {'works': Work.objects.all()})

def workpage_detailed(request, id):
    return render_to_response("work_detailed.html", {'work': Work.objects.filter(id=id)[0]})