from django.urls import path
from . import views

urlpatterns = [

    path('create-institution/', views.create_institution, name='create-institution'),
    path('get-institutions/', views.get_institutions, name='get-institutions'),
    path('get-institution/', views.get_institution, name='get-institution'),
    path('update-institution/', views.update_institution, name='update-institution'),
    path('delete-institution/', views.delete_institution, name='delete-institution'),
    path('course-country-institution/', views.get_course_country_institution, name='get_course_country_institution'),

]