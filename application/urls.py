from django.urls import path
from . import views

urlpatterns = [
    path('create-document/', views.create_document, name='create_document'),
    path('get-document/', views.get_document, name='get_document'),
    path('get-documents/', views.get_documents, name='get_documents'),
    path('update-document/', views.update_document, name='update_document'),
    path('delete-document/', views.delete_document, name='delete_document'),
    path('create-applicant/', views.create_applicant, name='create_applicant'),
    path('get-applicant/', views.get_applicant, name='get_applicant'),
    path('get-applicants/', views.get_applicants, name='get_applicants'),
    path('update-applicant/', views.update_applicant, name='update_applicant'),
    path('delete-applicant/', views.delete_applicant, name='delete_applicant'),
]
