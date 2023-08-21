from django.urls import path
from . import views

urlpatterns = [

    path('api/create-country/', views.create_country, name='create-country'),
    path('api/get-countries/', views.get_countries, name='get-countries'),
    path('api/get-country/', views.get_country, name='get-country'),
    path('api/update-country/', views.update_country, name='update-country'),
    path('api/delete-country/', views.delete_country, name='delete-country'),

    path('api/create-course/', views.create_course, name='create-course'),
    path('api/get-courses/', views.get_courses, name='get-courses'),
    path('api/get-course/', views.get_course, name='get-course'),
    path('api/update-course/', views.update_course, name='update-course'),
    path('api/delete-course/', views.delete_course, name='delete-course'),

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

    path('create-test/', views.create_test, name='create-test'),
    path('get-tests/', views.get_tests, name='get-tests'),
    path('get-test/', views.get_test, name='get-test'),
    path('update-test/', views.update_test, name='update-test'),
    path('delete-test/', views.delete_test, name='delete-test'),

    path('create-tag/', views.create_tag, name='create-tag'),
    path('get-tags/', views.get_tags, name='get-tags'),
    path('update-tag/', views.update_tag, name='update-tag'),
    path('delete-tag/', views.delete_tag, name='delete-tag'),

    path('create-event/', views.create_event, name='create-event'),
    path('get-events/', views.get_events, name='get-events'),
    path('get-event/', views.get_event, name='get-event'),
    path('update-event/', views.update_event, name='update-event'),
    path('delete-event/', views.delete_event, name='delete-event'),

    path('course-country-institution/', views.get_course_country_institution, name='get_course_country_institution'),
    path('course-country/', views.get_course_country, name='get_course_country'),

]