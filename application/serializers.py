from .models import Applicant, Document, Payment, Quote
from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    interested_country = serializers.StringRelatedField()
    interested_course = serializers.StringRelatedField()
    interested_institution = serializers.StringRelatedField()

    class Meta:
        model = Applicant
        fields = '__all__'


class ApplicantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['full_name',]


class ApplicantListSerializer(serializers.ModelSerializer):
    interested_country = serializers.StringRelatedField()
    interested_course = serializers.StringRelatedField()
    interested_institution = serializers.StringRelatedField()
    # documents = DocumentSerializer(many=True)

    class Meta:
        model = Applicant
        fields = ['id', 'status', 'full_name',  'phone_number', 'email', 'degree_title', 'degree_level',
                  'academic_score', 'address', 'interested_country', 'interested_course', 'interested_institution']


class QuoteSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField()

    class Meta:
        model = Quote
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = '__all__'
