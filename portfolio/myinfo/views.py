from django.shortcuts import render
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, "myinfo/index.html")


def skills(request):
    return render(request, "myinfo/skills.html")


def projects(request):
    return render(request, "myinfo/projects.html")


def education(request):
    return render(request, "myinfo/education.html")


def achivements(request):
    return render(request, "myinfo/achivements.html")
