from django.urls import path
from . import views

urlpatterns = [

    path('create-country/', views.create_country, name='create-country'),
    path('get-countries/', views.get_countries, name='get-countries'),
    path('get-country/', views.get_country, name='get-country'),
    path('update-country/', views.update_country, name='update-country'),
    path('delete-country/', views.delete_country, name='delete-country'),

    path('create-course-type/', views.create_course_type, name='create-course-type'),
    path('get-course-types/', views.get_course_types, name='get-course-types'),
    path('get-course-type/', views.get_course_type, name='get-course-type'),
    path('update-course-type/', views.update_course_type, name='update-course-type'),
    path('delete-course-type/', views.delete_course_type, name='delete-course-type'),

    path('create-course/', views.create_course, name='create-course'),
    path('get-courses/', views.get_courses, name='get-courses'),
    path('get-course/', views.get_course, name='get-course'),
    path('update-course/', views.update_course, name='update-course'),
    path('delete-course/', views.delete_course, name='delete-course'),

    path('create-institution/', views.create_institution, name='create-institution'),
    path('get-institutions/', views.get_institutions, name='get-institutions'),
    path('get-institution/', views.get_institution, name='get-institution'),
    path('update-institution/', views.update_institution, name='update-institution'),
    path('delete-institution/', views.delete_institution, name='delete-institution'),

    path('create-class-schedule/', views.create_class_schedule, name='create-class_schedule'),
    path('get-class-schedules/', views.get_class_schedules, name='get-class_schedules'),
    path('get-class-schedule/', views.get_class_schedule, name='get-class_schedule'),
    path('update-class-schedule/', views.update_class_schedule, name='update-class_schedule'),
    path('delete-class-schedule/', views.delete_class_schedule, name='delete-class_schedule'),

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