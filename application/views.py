from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from application.serializers import ApplicantListSerializer, ApplicantSerializer, DocumentSerializer
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
@permission_classes([IsAuthenticated])
def get_documents(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many =True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
    sat_score = request.POST.get('sat_score')
    other_language = request.POST.get('other_language')
    interested_country = request.POST['interested_country']
    interested_course = request.POST['interested_course']
    documents = request.FILES.getlist('documents')

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
        sat_score=sat_score,
        other_language=other_language,
        interested_country=interested_country,
        interested_course=interested_course
    )
    applicant.documents.set(documents)  

    applicant.save()

    return Response({"success": "Applicant created successfully"})


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def get_applicants(request):
    applicant = Applicant.objects.all()
    serializer = ApplicantListSerializer(applicant, many =True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_applicant(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)
    serializer = ApplicantSerializer(applicant)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_applicant(request):
    id = request.GET.get("id")

    applicant = Applicant.objects.get(id=id)
    applicant_purpose = request.POST.get('applicant_purpose')
    full_name = request.POST.get('full_name')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    dob = request.POST.get('dob')
    institution = request.POST.get('institution')
    degree_title = request.POST.get('degree_title')
    degree_level = request.POST.get('degree_level')
    passed_year = request.POST.get('passed_year')
    course_start_date = request.POST.get('course_start_date')
    course_end_date = request.POST.get('course_end_date')
    academic_score_category = request.POST.get('academic_score_category')
    academic_score = request.POST.get('academic_score')
    address = request.POST.get('address')
    ielts_score = request.POST.get('ielts_score')
    toefl_score = request.POST.get('toefl_score')
    pte_score = request.POST.get('pte_score')
    gre_score = request.POST.get('gre_score')
    sat_score = request.POST.get('sat_score')
    other_language = request.POST.get('other_language')
    interested_country = request.POST.get('interested_country')
    interested_course = request.POST.get('interested_course')
    new_status = request.POST.get('status')
    documents = request.FILES.getlist('documents')

    current_status = applicant.status
    allowed_status_transitions = {
        'Interested': ['Created'],
        'Created': ['Submitted'],
        'Submitted': ['Offer', 'Rejected'],
        'Offer': ['Visa Created', 'Rejected'],
        'Visa Created': ['Visa Submitted'],
        'Visa Submitted': ['Docs Requested', 'Granted'],
        'Docs Requested': ['Granted'],
        'Granted': ['Enrolled'],
        'Rejected': [],
        'Enrolled': [],
    }

    if current_status not in allowed_status_transitions:
        return Response({"error": "Invalid current status"}, status=status.HTTP_400_BAD_REQUEST)

    if new_status not in allowed_status_transitions[current_status]:
        return Response({"error": "Invalid status transition"}, status=status.HTTP_400_BAD_REQUEST)

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
    applicant.sat_score = sat_score
    applicant.other_language = other_language
    applicant.interested_country = interested_country
    applicant.interested_course = interested_course
    applicant.status = new_status
    applicant.save()

    applicant.documents.set(documents)  

    return Response({"success": "Applicant updated successfully"})
    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_applicant(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)
    applicant.delete()
    return Response({"success": "Applicant deleted successfully"})
    
