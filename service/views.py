from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from service.models import Country, Course, Institution, ClassSchedule
from service.serializers import CountrySerializer, CourseSerializer, InstitutionSerializer, ClassScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from .models import Institution, Country, Course
from .serializers import InstitutionListSerializer, InstitutionSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_class_schedule(request):
    name = request.POST.get('name')
    test_type = request.POST.get('test_type')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    price = request.POST.get('price')
    max_capacity = request.POST.get('max_capacity')
    instructor = request.POST.get('instructor')
    classroom = request.POST.get('classroom')

    class_schedule = ClassSchedule.objects.create(
        name=name,
        test_type=test_type,
        start_date=start_date,
        end_date=end_date,
        start_time=start_time,
        end_time=end_time,
        price=price,
        max_capacity=max_capacity,
        instructor=instructor,
        classroom=classroom
    )
    class_schedule.save()
    return Response({"success": "Class Schedule created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_class_schedules(request):
    class_schedules = ClassSchedule.objects.all()
    serializer = ClassScheduleSerializer(class_schedules, many=True)
    return Response({"class_schedules": serializer.data})


@api_view(["GET"])
def get_class_schedule(request):
    id = request.GET.get("id")
    class_schedule = ClassSchedule.objects.get(id=id)

    try:
        class_schedule = ClassSchedule.objects.filter(class_schedule=class_schedule)
        serializer = ClassScheduleSerializer(class_schedule)
        return Response(serializer.data)
    except class_schedule.DoesNotExist:
        return Response({"error": "class_schedule not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_class_schedule(request):
    id = request.POST.get("id")
    try:
        class_schedule = ClassSchedule.objects.get(id=id)
    except ClassSchedule.DoesNotExist:
        return Response({"error": "ClassSchedule not found."}, status=status.HTTP_404_NOT_FOUND)

    name = request.POST.get('name')
    test_type = request.POST.get('test_type')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    price = request.POST.get('price')
    max_capacity = request.POST.get('max_capacity')
    instructor = request.POST.get('instructor')
    classroom = request.POST.get('classroom')

    class_schedule.name = name
    class_schedule.test_type = test_type
    class_schedule.start_date = start_date
    class_schedule.end_date = end_date
    class_schedule.start_time = start_time
    class_schedule.end_time = end_time
    class_schedule.price = price
    class_schedule.max_capacity = max_capacity
    class_schedule.instructor = instructor
    class_schedule.classroom = classroom

    class_schedule.save()

    return Response({"success": "Class Schedule updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_class_schedule(request):
    id = request.GET.get("id")
    
    class_schedule = ClassSchedule.objects.get(id=id)
    class_schedule.delete()
    return Response({"success": "ClassSchedule deleted successfully"})


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_institution(request):
    institution_name = request.POST.get('institution_name')
    country = request.POST.get('intrested_country')
    courses = request.POST.getlist('intrested_course') 
    website = request.POST.get('website')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    # logo = request.FILES.get('logo

    try:
        country = Country.objects.get(country_name=country)
    except Country.DoesNotExist:
        return Response({"error": "Country not found."}, status=status.HTTP_400_BAD_REQUEST)

    institution = Institution.objects.create(
        institution_name=institution_name,
        country=country,        
        website=website,
        email=email,
        contact=contact,
        address=address,
        # logo=logo
    )
    
    courses_to_add = Course.objects.filter(course_name__in=courses)
    institution.courses.set(courses_to_add)
    institution.save()
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
        return Response({"error": "Institution not found."}, status=status.HTTP_404_NOT_FOUND)

    institution_name = request.POST.get('institution_name')
    country_id = request.POST.get('country_id')
    courses = request.POST.getlist('courses')  # Assuming multiple courses can be selected
    website = request.POST.get('website')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    # logo = request.FILES.get('logo')

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
    # institution.logo = logo
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
        "interested_institution": inserializer.data
    })


@api_view(["GET"])
def get_course_country(request):
    counrty = Country.objects.all()
    counserializer = CountrySerializer(counrty, many=True)
    course = Course.objects.all()
    coserializer = CourseSerializer(course, many=True)

    return Response({
        "interested_country": counserializer.data,
        "interested_course": coserializer.data
    })

