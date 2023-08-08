from .models import Applicant, Document
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
    class Meta:
        model = Applicant
        fields = ['id', 'full_name', 'phone_number', 'email', 'degree_title', 'degree_level', 'academic_score', 'address', 'interested_country', 'interested_course', 'interested_institution']
