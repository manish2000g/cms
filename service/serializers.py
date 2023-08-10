
from rest_framework import serializers
from .models import Country, Course, Institution

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name',)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_name',)

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('institution_name',)

class InstitutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


