from django.contrib import admin

from application.models import Applicant, Document

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Document)
