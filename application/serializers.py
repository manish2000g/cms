from .models import Applicant, Document, Payment
from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class ApplicantListSerializer(serializers.ModelSerializer):
    interested_country = serializers.StringRelatedField()
    interested_course = serializers.StringRelatedField()
    interested_institution = serializers.StringRelatedField()
    class Meta:
        model = Applicant
        fields = ['id', 'logo', 'full_name', 'phone_number', 'email', 'degree_title', 'degree_level', 'academic_score', 'address', 'interested_country', 'interested_course', 'interested_institution']

class PaymentSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField()
    class Meta:
        model = Payment
        fields = '__all__'

