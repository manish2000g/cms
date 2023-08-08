from django.urls import path
from . import views

urlpatterns = [

    path('course-country-institution/', views.get_course_country_institution, name='get_course_country_institution'),

]