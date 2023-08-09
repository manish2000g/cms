from django.contrib import admin

from application.models import Applicant, Commission, Document, Payment

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Document)
admin.site.register(Payment)
admin.site.register(Commission)
