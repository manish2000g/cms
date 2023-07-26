from django.urls import path
from . import views

urlpatterns = [
    path('create-application/', views.create_application, name='create_application'),
    path('get-application/', views.get_application, name='get_application'),
    path('update-application/', views.update_application, name='update_application'),
    path('delete-application/', views.delete_application, name='delete_application'),
]
