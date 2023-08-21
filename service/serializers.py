
from rest_framework import serializers
from .models import ClassSchedule, Country, Course, Event, Institution, Tag, Test


class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSchedule
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class_schedule = serializers.StringRelatedField()
    class Meta:
        model = Test
        fields = '__all__'

        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'


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
    country = CountrySerializer(read_only=True)
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Institution
        fields = '__all__'


