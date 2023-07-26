from .models import Applicant
from rest_framework import serializers


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class ApplicantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['full_name', 'phone_number', 'email', 'degree_title', 'degree_level', 'academic_score', 'address', 'interested_country', 'interested_course']
