from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from service.models import Country, Course, Institution
from service.serializers import CountrySerializer, CourseSerializer, InstitutionSerializer


@api_view(["GET"])
def get_course_country_institution(request):
    counrty = Country.objects.all()
    counserializer = CountrySerializer(counrty, many=True)
    course = Course.objects.all()
    coserializer = CourseSerializer(course, many=True)
    institution = Institution.objects.all()
    inserializer = InstitutionSerializer(institution, many=True)

    return Response({
        "interested_country": counserializer.data,
        "interested_course": coserializer.data,
        "institution_name": inserializer.data
    })