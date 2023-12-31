from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from service.models import Country, Course, Institution, ClassSchedule
from service.serializers import CountrySerializer, CourseSerializer, InstitutionSerializer, ClassScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from .models import CourseType, EnglishProfficiency, Event, Institution, Country, Course, Tag, Test
from .serializers import CountryListSerializer, CourseListSerializer, CourseTypeSerializer, EnglishProfficiencySerializer, EventSerializer, InstitutionListSerializer, InstitutionSerializer, TagSerializer, TestSerializer, TestTypeSerializer


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_class_schedule(request):
    class_name = request.POST.get('class_name')
    test = request.POST.get('test_type')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    price = request.POST.get('price')
    max_capacity = request.POST.get('max_capacity')
    instructor = request.POST.get('instructor')

    class_schedule = ClassSchedule.objects.create(
        class_name=class_name,
        test=test,
        start_date=start_date,
        end_date=end_date,
        start_time=start_time,
        end_time=end_time,
        price=price,
        max_capacity=max_capacity,
        instructor=instructor,
    )
    class_schedule.save()
    return Response({"success": "Class Schedule created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_class_schedules(request):
    class_schedules = ClassSchedule.objects.all()
    serializer = ClassScheduleSerializer(class_schedules, many=True)
    return Response({"class_schedules": serializer.data})


@api_view(["GET"])
def get_test_type(request):
    test_types = ClassSchedule.objects.all()
    serializer = TestTypeSerializer(test_types, many=True)
    return Response({"test_type": serializer.data})


@api_view(["GET"])
def get_class_schedule(request):
    id = request.GET.get("id")
    class_schedule = ClassSchedule.objects.get(id=id)

    try:
        class_schedule = ClassSchedule.objects.filter(
            class_schedule=class_schedule)
        serializer = ClassScheduleSerializer(class_schedule)
        return Response(serializer.data)
    except class_schedule.DoesNotExist:
        return Response({"error": "class_schedule not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def update_class_schedule(request):
    id = request.POST.get("id")
    try:
        class_schedule = ClassSchedule.objects.get(id=id)
    except ClassSchedule.DoesNotExist:
        return Response({"error": "ClassSchedule not found."}, status=status.HTTP_404_NOT_FOUND)

    class_name = request.POST.get('class_name')
    test = request.POST.get('test_type')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    price = request.POST.get('price')
    max_capacity = request.POST.get('max_capacity')
    instructor = request.POST.get('instructor')

    class_schedule.class_name = class_name
    class_schedule.test = test
    class_schedule.start_date = start_date
    class_schedule.end_date = end_date
    class_schedule.start_time = start_time
    class_schedule.end_time = end_time
    class_schedule.price = price
    class_schedule.max_capacity = max_capacity
    class_schedule.instructor = instructor

    class_schedule.save()

    return Response({"success": "Class Schedule updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
def delete_class_schedule(request):
    id = request.GET.get("id")

    class_schedule = ClassSchedule.objects.get(id=id)
    class_schedule.delete()
    return Response({"success": "ClassSchedule deleted successfully"})


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_test(request):
    test_type_name = request.POST.get('test_type')
    description = request.POST.get('description')
    test_date = request.POST.get('test_date')
    test_time = request.POST.get('test_time')
    max_capacity = request.POST.get('max_capacity')
    result_date = request.POST.get('result_date')

    try:
        test_type = ClassSchedule.objects.get(test=test_type_name)
    except ClassSchedule.DoesNotExist:
        return Response({"error": "Test Type not found."}, status=status.HTTP_400_BAD_REQUEST)

    test = Test.objects.create(
        test_type=test_type,
        description=description,
        test_date=test_date,
        test_time=test_time,
        max_capacity=max_capacity,
        result_date=result_date
    )
    test.save()
    return Response({"success": "Test created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_tests(request):
    tests = Test.objects.all()
    serializer = TestSerializer(tests, many=True)
    return Response({"tests": serializer.data})


@api_view(["GET"])
def get_test(request):
    test_id = request.GET.get("id")

    try:
        test = Test.objects.get(id=test_id)
        serializer = TestSerializer(test)
        return Response(serializer.data)
    except Test.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def update_test(request):
    test_id = request.POST.get("test_id")

    try:
        test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    test_type_name = request.POST.get('test_type')
    description = request.POST.get('description')
    test_date = request.POST.get('test_date')
    test_time = request.POST.get('test_time')
    max_capacity = request.POST.get('max_capacity')
    result_date = request.POST.get('result_date')

    try:
        test_type = ClassSchedule.objects.get(test=test_type_name)
    except ClassSchedule.DoesNotExist:
        return Response({"error": "Test Type not found."}, status=status.HTTP_400_BAD_REQUEST)

    test.test_type = test_type
    test.description = description
    test.test_date = test_date
    test.test_time = test_time
    test.max_capacity = max_capacity
    test.result_date = result_date

    test.save()

    return Response({"success": "Test updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
def delete_test(request):
    test_id = request.GET.get("id")

    try:
        test = Test.objects.get(id=test_id)
        test.delete()
        return Response({"success": "Test deleted successfully"})
    except Test.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_country(request):
    country_name = request.POST.get('country_name')
    description = request.POST.get('description')

    country = Country.objects.create(
        country_name=country_name,
        description=description
    )
    country.save()

    return Response({"success": "Country created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_countries(request):
    countries = Country.objects.all()
    serializer = CountryListSerializer(countries, many=True)
    return Response({"countries": serializer.data})


@api_view(["GET"])
def get_country(request):
    country_id = request.GET.get("id")

    try:
        country = Country.objects.get(id=country_id)
        serializer = CountryListSerializer(country)
        return Response(serializer.data)
    except Country.DoesNotExist:
        return Response({"error": "Country not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
# @permission_classes([IsAuthenticated])
def update_country(request):
    country_id = request.POST.get("country_id")

    try:
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist:
        return Response({"error": "Country not found."}, status=status.HTTP_404_NOT_FOUND)

    country_name = request.POST.get('country_name')
    description = request.POST.get('description')

    country.country_name = country_name
    country.description = description

    country.save()

    return Response({"success": "Country updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
def delete_country(request):
    country_id = request.GET.get("id")

    try:
        country = Country.objects.get(id=country_id)
        country.delete()
        return Response({"success": "Country deleted successfully"})
    except Country.DoesNotExist:
        return Response({"error": "Country not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def create_course_type(request):
    course_type = request.POST.get('degree')

    course_type = CourseType.objects.create(course_type=course_type)
    course_type.save()
    return Response({"success": "Course Type created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_course_types(request):
    course_types = CourseType.objects.all()
    serializer = CourseTypeSerializer(course_types, many=True)

    return Response({
        "course_types": serializer.data})


@api_view(["GET"])
def get_course_type(request):
    id = request.GET.get('id')
    try:
        course_type = CourseType.objects.get(id=id)
    except CourseType.DoesNotExist:
        return Response({"error": "Course Type not found."}, status=status.HTTP_404_NOT_FOUND)

    # Assuming you have a serializer for CourseType
    serializer = CourseTypeSerializer(course_type)

    return Response(serializer.data)


@api_view(["PUT"])
def update_course_type(request):
    id = request.data.get('id')  # Use request.data for update
    try:
        course_type = CourseType.objects.get(id=id)
    except CourseType.DoesNotExist:
        return Response({"error": "Course Type not found."}, status=status.HTTP_404_NOT_FOUND)

    degree = request.data.get('degree')
    course_type.degree = degree
    course_type.save()

    return Response({"success": "Course Type updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_course_type(request):
    id = request.data.get('id')
    try:
        course_type = CourseType.objects.get(id=id)
    except CourseType.DoesNotExist:
        return Response({"error": "Course Type not found."}, status=status.HTTP_404_NOT_FOUND)
    course_type.delete()
    return Response({"success": "Course Type deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_course(request):
    course_name = request.POST.get('course_name')
    cdegree = request.POST.get('degree')

    description = request.POST.get('description')
    course_start_date = request.POST.get('course_start_date')
    course_end_date = request.POST.get('course_end_date')
    application_deadline = request.POST.get('application_deadline')
    # course_image = request.FILES.get('course_image')

    try:
        degree = CourseType.objects.get(course_type=cdegree)
    except CourseType.DoesNotExist:
        return Response({"error": "Degree not found."}, status=status.HTTP_400_BAD_REQUEST)

    course = Course.objects.create(
        course_name=course_name,
        degree=degree,
        description=description,
        course_start_date=course_start_date,
        course_end_date=course_end_date,
        application_deadline=application_deadline,
        # course_image=course_image
    )
    course.save()
    return Response({"success": "Course created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response({"courses": serializer.data})


@api_view(["GET"])
def get_course(request):
    course_id = request.GET.get("id")

    try:
        course = Course.objects.get(id=course_id)
        serializer = CourseListSerializer(course)
        return Response(serializer.data)
    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
# @permission_classes([IsAuthenticated])
def update_course(request):
    course_id = request.POST.get("course_id")

    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

    course_name = request.POST.get('course_name')
    cdegree = request.POST.get('degree')
    description = request.POST.get('description')
    course_start_date = request.POST.get('course_start_date')
    course_end_date = request.POST.get('course_end_date')
    application_deadline = request.POST.get('application_deadline')
    # course_image = request.FILES.get('course_image')

    try:
        degree = CourseType.objects.get(degree=cdegree)
    except CourseType.DoesNotExist:
        return Response({"error": "Degree not found."}, status=status.HTTP_400_BAD_REQUEST)

    course.course_name = course_name
    course.description = description
    course.degree = degree
    course.course_start_date = course_start_date
    course.course_end_date = course_end_date
    course.application_deadline = application_deadline
    # course.course_image = course_image

    course.save()
    return Response({"success": "Course updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
def delete_course(request):
    course_id = request.GET.get("id")

    try:
        course = Course.objects.get(id=course_id)
        course.delete()
        return Response({"success": "Course deleted successfully"})
    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_institution(request):
    institution_name = request.POST.get('institution_name')
    country = request.POST.get('interested_country')
    courses = request.POST.getlist('courses')
    website = request.POST.get('website')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    min_gpa = request.POST.get('min_gpa')
    min_english_score = request.POST.get('min_english_score')
    english_profficiency = request.POST.get('english_profficiency')
    # logo = request.FILES.get('logo

    try:
        country = Country.objects.get(country_name=country)
        english_profficiency = EnglishProfficiency.objects.get(english_profficiency=english_profficiency)
    except Country and EnglishProfficiency.DoesNotExist:
        return Response({"error": "Country or EnglishProfficiency not found."}, status=status.HTTP_400_BAD_REQUEST)

    institution = Institution.objects.create(
        institution_name=institution_name,
        country=country,
        website=website,
        email=email,
        contact=contact,
        address=address,
        min_gpa=min_gpa,
        min_english_score=min_english_score,
        english_profficiency=english_profficiency,
        # logo=logo
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
def get_english_profficiency(request):
    english_profficiency = EnglishProfficiency.objects.all()
    serializer = EnglishProfficiencySerializer(english_profficiency, many=True)
    return Response({
        "english_profficiency": serializer.data
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


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def update_institution(request):
    institution_id = request.POST.get("institution_id")

    try:
        institution = Institution.objects.get(id=institution_id)
    except Institution.DoesNotExist:
        return Response({"error": "Institution not found."}, status=status.HTTP_404_NOT_FOUND)

    institution_name = request.POST.get('institution_name')
    country = request.POST.get('intrested_country')
    courses = request.POST.getlist('interested_course')
    website = request.POST.get('website')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    # logo = request.FILES.get('logo')

    try:
        country = Country.objects.get(country_name=country)
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
# @permission_classes([IsAuthenticated])
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
    english_profficiency = EnglishProfficiency.objects.all()
    epserializer = EnglishProfficiencySerializer(english_profficiency, many=True)

    return Response({
        "interested_country": counserializer.data,
        "interested_course": coserializer.data,
        "english_profficiency": epserializer.data
    })


@api_view(["POST"])
def create_tag(request):
    tag_name = request.POST.get('tag_name')

    tag = Tag.objects.create(
        tag_name=tag_name,
    )
    tag.save()
    return Response({"success": "Tag created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_tags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response({
        "tags": serializer.data})


@api_view(["POST"])
def update_tag(request):
    tag_id = request.POST.get("tag_id")
    try:
        tag = Tag.objects.get(id=tag_id)
    except Tag.DoesNotExist:
        return Response({"error": "Tag not found."}, status=status.HTTP_404_NOT_FOUND)

    tag_name = request.POST.get('tag_name')

    tag.tag_name = tag_name
    tag.save()
    return Response({"success": "Tag updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_tag(request):
    id = request.GET.get("id")

    tag = Tag.objects.get(id=id)
    tag.delete()
    return Response({"success": "Tag deleted successfully"})


@api_view(["POST"])
def create_event(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    date = request.POST.get('date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    event_status = request.POST.get('event_status')
    # tags = request.POST.getlist('tags')

    event = Event.objects.create(
        name=name,
        description=description,
        date=date,
        start_time=start_time,
        end_time=end_time,
        location=location,
        capacity=capacity,
        event_status=event_status
    )
    # # Retrieve all existing tags
    # existing_tags = Tag.objects.filter(Q(tag_name__in=tags))

    # # Create new tags for any missing tags
    # missing_tags = set(tags) - set(existing_tags.values_list('tag_name', flat=True))
    # new_tags = [Tag(tag_name=tag_name) for tag_name in missing_tags]
    # Tag.objects.bulk_create(new_tags)

    # # Add all tags (existing and new) to the article
    # tags_to_add = existing_tags.union(Tag.objects.filter(Q(tag_name__in=missing_tags)))
    # event.tags.add(*tags_to_add)
    return Response({"success": "Event created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({
        "events": serializer.data})


@api_view(["GET"])
def get_event(request):
    id = request.GET.get("id")
    event = Event.objects.get(id=id)
    serializer = EventSerializer(event)
    return Response(serializer.data)


@api_view(["POST"])
def update_event(request):
    event_id = request.POST.get("event_id")

    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

    name = request.POST.get('name')
    description = request.POST.get('description')
    date = request.POST.get('date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    event_status = request.POST.get('event_status')
    # tags = request.POST.getlist('tags')

    event.name = name
    event.description = description
    event.date = date
    event.start_time = start_time
    event.end_time = end_time
    event.location = location
    event.capacity = capacity
    event.event_status = event_status

    # existing_tags = Tag.objects.filter(Q(tag_name__in=tags))

    # missing_tags = set(tags) - set(existing_tags.values_list('tag_name', flat=True))
    # new_tags = [Tag(tag_name=tag_name) for tag_name in missing_tags]
    # Tag.objects.bulk_create(new_tags)

    # tags_to_add = existing_tags.union(Tag.objects.filter(Q(tag_name__in=missing_tags)))
    # event.tags.set(*tags_to_add)
    event.save()
    return Response({"success": "Event updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_event(request):
    id = request.GET.get("id")

    event = Event.objects.get(id=id)
    event.delete()
    return Response({"success": "Event deleted successfully"})
