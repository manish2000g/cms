from django.contrib import admin

from service.models import Country, Course, Enquiry, Event, Service, Tag

# Register your models here.

admin.site.register(Service)
admin.site.register(Country)
admin.site.register(Course)
admin.site.register(Enquiry)
admin.site.register(Tag)
admin.site.register(Event)
