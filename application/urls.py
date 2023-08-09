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
    path('create-payment/', views.create_payment, name='create_payment'),
    path('get-payment/', views.get_payment, name='get_payment'),
    path('get-payments/', views.get_payments, name='get_payments'),
    path('update-payment/', views.update_payment, name='update_payment'),
    path('delete-payment/', views.delete_payment, name='delete_payment'),
]
