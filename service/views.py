from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from service.models import Country, Course, Institution
from service.serializers import CountrySerializer, CourseSerializer, InstitutionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from .models import Institution, Country, Course
from .serializers import InstitutionListSerializer, InstitutionSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_institution(request):
    institution_name = request.POST.get('institution_name')
    country = request.POST.get('country_id')
    courses = request.POST.getlist('courses')  
    website = request.POST.get('website')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    logo = request.FILES.get('logo')

    try:
        country = Country.objects.get(id=country)
    except Country.DoesNotExist:
        return Response({"error": "Country not found."}, status=status.HTTP_400_BAD_REQUEST)

    institution = Institution(
        institution_name=institution_name,
        country=country,        
        website=website,
        email=email,
        contact=contact,
        address=address,
        logo=logo
    )
    
    for course_id in courses:
            course = Course.objects.get(id=course_id)
            institution.courses.add(course)  

    return Response({"success": "Institution created successfully"}, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_institutions(request):
    institutions = Institution.objects.all()
    serializer = InstitutionListSerializer(institutions, many=True)
    return Response({
        "institutions": serializer.data
    })

@api_view(["GET"])
def get_institution(request):
    id = request.GET.get("id")
    institution = Institution.objects.get(id=id)

    try:
        institution = Institution.objects.filter(institution=institution)
        serializer = InstitutionListSerializer(institution)
        return Response(serializer.data)
    except Institution.DoesNotExist:
        return Response({"error": "Institution not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_institution(request):
    institution_id = request.POST.get("institution_id")

    try:
        institution = Institution.objects.get(id=institution_id)
    except Institution.DoesNotExist:
        return Response({"error": "Institution_id not found."}, status=status.HTTP_404_NOT_FOUND)

    institution_name = request.POST.get('institution_name')
    country_id = request.POST.get('country_id')
    courses = request.POST.getlist('courses')  # Assuming multiple courses can be selected
    website = request.POST.get('website')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    logo = request.FILES.get('logo')

    try:
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist:
        return Response({"error": "Country not found."}, status=status.HTTP_400_BAD_REQUEST)

    institution.institution_name = institution_name
    institution.country = country
    institution.website = website
    institution.email = email
    institution.contact = contact
    institution.address = address
    institution.logo = logo
    institution.courses.clear()

    for course_id in courses:
            course = Course.objects.get(id=course_id)
            institution.courses.add(course)

    institution.save()

    return Response({"success": "Institution updated successfully"}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_institution(request):
    id = request.GET.get("id")
    
    institution = Institution.objects.get(id=id)
    institution.delete()
    return Response({"success": "Institution deleted successfully"})

 
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

