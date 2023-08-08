
from rest_framework import serializers
from .models import Country, Course, Institution

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name')

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name')
