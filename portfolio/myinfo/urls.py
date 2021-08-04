
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('achivements/', views.achivements, name='achivements'),
]
