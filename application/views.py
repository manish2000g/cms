from .models import Payment, Invoice
from datetime import timedelta
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from .serializers import ApplicantNameSerializer, QuoteSerializer
from .models import Invoice, Quote
from rest_framework.decorators import api_view
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError
from application.serializers import ApplicantListSerializer, ApplicantSerializer, DocumentSerializer, PaymentSerializer
from service.models import Country, Course, Institution
from .models import Applicant, Document, Payment


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_document(request):
    title = request.POST.get('title')
    file = request.FILES.get('file')

    document = Document.objects.create(title=title, file=file)
    document.save()

    return Response({"success": "Document created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_documents(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    return Response({
        "documents": serializer.data})


@api_view(["GET"])
def get_document(request):
    id = request.GET.get("id")
    document = Document.objects.get(id=id)
    serializer = DocumentSerializer(document)
    return Response(serializer.data)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def update_document(request):
    id = request.GET.get("id")

    document = Document.objects.get(id=id)
    title = request.POST.get('title')
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
    applicant_purpose = request.POST.get('applicant_purpose')
    logo = request.FILES.get('logo')

    status = request.POST.get('status', 'Created')
    full_name = request.POST.get('full_name')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
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
    gmat_score = request.POST.get('gmat_score')
    sat_score = request.POST.get('sat_score')
    other_language = request.POST.get('other_language')
    interested_country = request.POST.get('interested_country')
    interested_course = request.POST.get('interested_course')
    documents = request.FILES.getlist('documents')
    interested_institution = request.POST.get('interested_institution')

    try:

        interested_course = Course.objects.get(course_name=interested_course)
        interested_country = Country.objects.get(
            country_name=interested_country)
        interested_institution = Institution.objects.get(
            institution_name=interested_institution)

    except (Country.DoesNotExist, Course.DoesNotExist, Institution.DoesNotExist):
        return Response({"error": "Invalid country, course, or institution provided."}, status=400)

    applicant = Applicant.objects.create(
        applicant_purpose=applicant_purpose,
        logo=logo,
        status=status,
        full_name=full_name,
        phone_number=phone_number,
        email=email,
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
    serializer = ApplicantListSerializer(applicant, many=True)
    return Response({
        'applicants': serializer.data
    })

# get applicant name for quote


@api_view(["GET"])
def get_applicant_names(request):
    applicant = Applicant.objects.all()
    serializer = ApplicantNameSerializer(applicant, many=True)
    return Response({
        'applicant': serializer.data
    })


@api_view(["GET"])
def get_applicant(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)
    serializer = ApplicantSerializer(applicant)
    return Response(serializer.data)


@api_view(["POST"])
def update_applicant_status(request):
    # Parse the JSON data from the request body
    data = json.loads(request.body)
    id = data.get('id')
    print(id)
    try:
        applicant = Applicant.objects.get(id=id)
    except Applicant.DoesNotExist:
        return Response({"error": "Applicant not found"}, status=404)
    status = data.get('newStatus')
    applicant.status = status
    applicant.save()
    return Response({"success": 'Applicant Updated successfully'})


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def update_applicant(request):
    id = request.POST.get("id")
    try:
        applicant = Applicant.objects.get(id=id)
    except Applicant.DoesNotExist:
        return Response({"error": "Applicant not found"}, status=404)

    applicant_purpose = request.POST.get('applicant_purpose')
    logo = request.FILES.get('logo')
    status = request.POST.get('status', 'Created')
    full_name = request.POST.get('full_name')
    phone_number = request.POST.get('phone_number',)
    email = request.POST.get('email')
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
    gmat_score = request.POST.get('gmat_score')
    sat_score = request.POST.get('sat_score')
    other_language = request.POST.get('other_language')
    country_name = request.POST.get('interested_country')
    course_name = request.POST.get('interested_course')
    institution_name = request.POST.get('interested_institution')

    try:
        interested_country = Country.objects.get(country_name=country_name)
        interested_course = Course.objects.get(course_name=course_name)
        interested_institution = Institution.objects.get(
            institution_name=institution_name)
    except (Country.DoesNotExist, Course.DoesNotExist, Institution.DoesNotExist):
        return Response({"error": "Invalid country, course, or institution provided."}, status=400)

    applicant.applicant_purpose = applicant_purpose
    applicant.logo = logo
    applicant.status = status
    applicant.full_name = full_name
    applicant.phone_number = phone_number
    applicant.email = email
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
# @permission_classes([IsAuthenticated])
def delete_applicant(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)
    applicant.delete()
    return Response({"success": "Applicant deleted successfully"})


@api_view(["POST"])
def create_quote(request):
    applicantn = request.POST.get('applicant')
    quote_text = request.POST.get('quote')
    purpose = request.POST.get('purpose')
    due_date = request.POST.get('due_date')
    amount = request.POST.get('amount')

    try:
        applicant = Applicant.objects.get(full_name=applicantn)
    except Applicant.DoesNotExist:
        return Response({"error": "Applicant not found."}, status=status.HTTP_400_BAD_REQUEST)

    quote = Quote.objects.create(
        applicant=applicant,
        quote=quote_text,
        purpose=purpose,
        due_date=due_date,
        amount=amount
    )
    quote.save()

    subject = 'Quote Created'
    message = f'Hello {applicant.full_name},\n\nYour quote for the purpose of {purpose} has been created successfully with "RS.{amount}" amount and due date for {due_date}.'
    from_email = 'hreedhann9@gmail.com'
    recipient_list = [applicant.email]

    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)

    return Response({"success": "Quote created successfully and email sent"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_quotes(request):
    quotes = Quote.objects.all()
    serializer = QuoteSerializer(quotes, many=True)
    return Response({"quotes": serializer.data})


@api_view(["GET"])
def get_quote(request):
    quote_id = request.GET.get("id")

    try:
        quote = Quote.objects.get(id=quote_id)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)
    except Quote.DoesNotExist:
        return Response({"error": "Quote not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_quote(request):
    quote_id = request.POST.get("id")

    try:
        quote = Quote.objects.get(id=quote_id)
    except Quote.DoesNotExist:
        return Response({"error": "Quote not found."}, status=status.HTTP_404_NOT_FOUND)

    applicantn = request.POST.get('applicant')
    quote_text = request.POST.get('quote')
    purpose = request.POST.get('purpose')
    due_date = request.POST.get('due_date')
    amount = request.POST.get('amount')

    try:
        applicant = Applicant.objects.get(full_name=applicantn)
    except Applicant.DoesNotExist:
        return Response({"error": "Applicant not found."}, status=status.HTTP_400_BAD_REQUEST)

    quote.applicant = applicant
    quote.quote = quote_text
    quote.purpose = purpose
    quote.due_date = due_date
    quote.amount = amount

    quote.save()

    return Response({"success": "Quote updated successfully"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_quote(request):
    quote_id = request.GET.get("id")

    try:
        quote = Quote.objects.get(id=quote_id)
        quote.delete()
        return Response({"success": "Quote deleted successfully"})
    except Quote.DoesNotExist:
        return Response({"error": "Quote not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create_payment(request):
    applicantn = request.POST.get('applicant')
    total_amount = request.data.get('total_amount')
    remaining_amount = request.data.get('remaining_amount')
    payment_status = request.data.get('payment_status')
    action = request.data.get('action')
    due_date = request.data.get('due_date')
    description = request.data.get('description')

    try:
        applicant = Applicant.objects.get(full_name=applicantn)
    except Applicant.DoesNotExist:
        return Response({"error": "Applicant not found."}, status=status.HTTP_400_BAD_REQUEST)

    # Create the payment
    payment = Payment.objects.create(
        applicant=applicant,
        total_amount=total_amount,
        remaining_amount=remaining_amount,
        payment_status=payment_status,
        action=action,
        due_date=due_date,
        description=description
    )

    # Create an associated invoice
    invoice = Invoice.objects.create(
        applicant=applicant,
        invoice_number=payment.id,
        issue_date=due_date,
        amount=total_amount,
        description=description
    )

    return Response({"success": "Payment and invoice created successfully"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_payments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response({
        "payments": serializer.data
    })


@api_view(["GET"])
def get_payment(request):
    id = request.GET.get("id")
    applicant = Applicant.objects.get(id=id)

    try:
        payment = Payment.objects.filter(applicant=applicant)
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def update_payment(request):
    payment_id = request.POST.get("payment_id")

    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

    try:
        applicant_id = request.POST.get('applicant_id')
        description = request.POST.get('description')
        total_amount = request.POST.get('total_amount')
        remaining_amount = request.POST.get('remaining_amount')
        payment_status = request.POST.get('payment_status')
        action = request.POST.get('action')
        due_date = request.POST.get('due_date')

        try:
            applicant = Applicant.objects.get(id=applicant_id)
        except Applicant.DoesNotExist:
            return Response({"error": "Applicant does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        payment.applicant = applicant
        payment.description = description
        payment.total_amount = total_amount
        payment.remaining_amount = remaining_amount
        payment.payment_status = payment_status
        payment.action = action
        payment.due_date = due_date

        payment.save()

        return Response({"success": "Payment updated successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
def delete_payment(request):
    id = request.GET.get("id")

    payment = Payment.objects.get(id=id)
    payment.delete()
    return Response({"success": "Payment deleted successfully"})
