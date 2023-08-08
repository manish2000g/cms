from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from application.serializers import ApplicantListSerializer, ApplicantSerializer, DocumentSerializer
from service.models import Country, Course, Institution
from .models import Applicant, Document


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_document(request):
    title = request.POST['title']
    file = request.FILES['file']

    document = Document.objects.create(title=title, file=file)
    document.save()

    return Response({"success": "Document created successfully"}, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_documents(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many =True)
    return Response({
        "documents": serializer.data})


@api_view(["GET"])
def get_document(request):
    id = request.GET.get("id")
    document = Document.objects.get(id=id)
    serializer = DocumentSerializer(document)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_document(request):
    id = request.GET.get("id")

    document = Document.objects.get(id=id)
    title = request.POST['title']
    file = request.FILES.get('file', document.file)

    document.title = title
    document.file = file
    document.save()

    return Response({"success": "Document updated successfully"}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_document(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)
    applicant.delete()
    return Response({"success": "Applicant deleted successfully"})

@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_applicant(request):
    applicant_purpose = request.POST['applicant_purpose']
    full_name = request.POST['full_name']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    dob = request.POST['dob']
    institution = request.POST['institution']
    degree_title = request.POST['degree_title']
    degree_level = request.POST['degree_level']
    passed_year = request.POST['passed_year']
    course_start_date = request.POST['course_start_date']
    course_end_date = request.POST['course_end_date']
    academic_score_category = request.POST['academic_score_category']
    academic_score = request.POST['academic_score']
    address = request.POST['address']
    ielts_score = request.POST.get('ielts_score')
    toefl_score = request.POST.get('toefl_score')
    pte_score = request.POST.get('pte_score')
    gre_score = request.POST.get('gre_score')
    gmat_score = request.POST.get('gmat_score')
    sat_score = request.POST.get('sat_score')
    other_language = request.POST.get('other_language')
    interested_country_id = request.POST['interested_country']
    interested_course_id = request.POST['interested_course']
    documents = request.FILES.getlist('documents')
    interested_institution_id = request.POST['interested_institution']

    try:
        interested_country = Country.objects.get(id=interested_country_id)
        interested_course = Course.objects.get(id=interested_course_id)
        interested_institution = Institution.objects.get(id=interested_institution_id)
    except (Country.DoesNotExist, Course.DoesNotExist, Institution.DoesNotExist):
        return Response({"error": "Invalid country, course, or institution provided."}, status=400)

    applicant = Applicant.objects.create(
        applicant_purpose=applicant_purpose,
        full_name=full_name,
        phone_number=phone_number,
        email=email,
        dob=dob,
        institution=institution,
        degree_title=degree_title,
        degree_level=degree_level,
        passed_year=passed_year,
        course_start_date=course_start_date,
        course_end_date=course_end_date,
        academic_score_category=academic_score_category,
        academic_score=academic_score,
        address=address,
        ielts_score=ielts_score,
        toefl_score=toefl_score,
        pte_score=pte_score,
        gre_score=gre_score,
        gmat_score=gmat_score,
        sat_score=sat_score,
        other_language=other_language,
        interested_country=interested_country,
        interested_course=interested_course,
        interested_institution=interested_institution
    )
    applicant.documents.set(documents)  
    applicant.save()

    return Response({"success": "Applicant created successfully"}, status=201)



@api_view(["GET"])
def get_applicants(request):
    applicant = Applicant.objects.all()
    serializer = ApplicantListSerializer(applicant, many =True)
    return Response({
        'applicants': serializer.data
    })


@api_view(["GET"])
def get_applicant(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)
    serializer = ApplicantSerializer(applicant)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_applicant(request, applicant_id):
    try:
        applicant = Applicant.objects.get(id=applicant_id)
    except Applicant.DoesNotExist:
        return Response({"error": "Applicant not found"}, status=404)

    applicant_purpose = request.data.get('applicant_purpose', applicant.applicant_purpose)
    full_name = request.data.get('full_name', applicant.full_name)
    phone_number = request.data.get('phone_number', applicant.phone_number)
    email = request.data.get('email', applicant.email)
    dob = request.data.get('dob', applicant.dob)
    institution = request.data.get('institution', applicant.institution)
    degree_title = request.data.get('degree_title', applicant.degree_title)
    degree_level = request.data.get('degree_level', applicant.degree_level)
    passed_year = request.data.get('passed_year', applicant.passed_year)
    course_start_date = request.data.get('course_start_date', applicant.course_start_date)
    course_end_date = request.data.get('course_end_date', applicant.course_end_date)
    academic_score_category = request.data.get('academic_score_category', applicant.academic_score_category)
    academic_score = request.data.get('academic_score', applicant.academic_score)
    address = request.data.get('address', applicant.address)
    ielts_score = request.data.get('ielts_score', applicant.ielts_score)
    toefl_score = request.data.get('toefl_score', applicant.toefl_score)
    pte_score = request.data.get('pte_score', applicant.pte_score)
    gre_score = request.data.get('gre_score', applicant.gre_score)
    gmat_score = request.data.get('gmat_score', applicant.gmat_score)
    sat_score = request.data.get('sat_score', applicant.sat_score)
    other_language = request.data.get('other_language', applicant.other_language)
    interested_country_id = request.data.get('interested_country', applicant.interested_country_id)
    interested_course_id = request.data.get('interested_course', applicant.interested_course_id)
    interested_institution_id = request.data.get('interested_institution', applicant.interested_institution_id)

    try:
        interested_country = Country.objects.get(id=interested_country_id)
        interested_course = Course.objects.get(id=interested_course_id)
        interested_institution = Institution.objects.get(id=interested_institution_id)
    except (Country.DoesNotExist, Course.DoesNotExist, Institution.DoesNotExist):
        return Response({"error": "Invalid country, course, or institution provided."}, status=400)

    applicant.applicant_purpose = applicant_purpose
    applicant.full_name = full_name
    applicant.phone_number = phone_number
    applicant.email = email
    applicant.dob = dob
    applicant.institution = institution
    applicant.degree_title = degree_title
    applicant.degree_level = degree_level
    applicant.passed_year = passed_year
    applicant.course_start_date = course_start_date
    applicant.course_end_date = course_end_date
    applicant.academic_score_category = academic_score_category
    applicant.academic_score = academic_score
    applicant.address = address
    applicant.ielts_score = ielts_score
    applicant.toefl_score = toefl_score
    applicant.pte_score = pte_score
    applicant.gre_score = gre_score
    applicant.gmat_score = gmat_score
    applicant.sat_score = sat_score
    applicant.other_language = other_language
    applicant.interested_country = interested_country
    applicant.interested_course = interested_course
    applicant.interested_institution = interested_institution

    applicant.save()

    return Response({"success": "Applicant updated successfully"}, status=200)

    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_applicant(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)
    applicant.delete()
    return Response({"success": "Applicant deleted successfully"})
    
