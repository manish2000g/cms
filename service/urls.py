from django.urls import path
from . import views

urlpatterns = [

    path('create-institution/', views.create_institution, name='create-institution'),
    path('get-institutions/', views.get_institutions, name='get-institutions'),
    path('get-institution/', views.get_institution, name='get-institution'),
    path('update-institution/', views.update_institution, name='update-institution'),
    path('delete-institution/', views.delete_institution, name='delete-institution'),
    path('create-class_schedule/', views.create_class_schedule, name='create-class_schedule'),
    path('get-class_schedules/', views.get_class_schedules, name='get-class_schedules'),
    path('get-class_schedule/', views.get_class_schedule, name='get-class_schedule'),
    path('update-class_schedule/', views.update_class_schedule, name='update-class_schedule'),
    path('delete-class_schedule/', views.delete_class_schedule, name='delete-class_schedule'),
    path('course-country-institution/', views.get_course_country_institution, name='get_course_country_institution'),

]