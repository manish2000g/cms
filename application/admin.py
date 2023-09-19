from django.contrib import admin

from application.models import Applicant, Commission, Document, Invoice, Payment, Quote

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Document)
admin.site.register(Payment)
admin.site.register(Commission)
admin.site.register(Quote)
admin.site.register(Invoice)

