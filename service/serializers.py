
from rest_framework import serializers
from .models import ClassSchedule, Country, Course, CourseType, Event, Institution, Tag, Test


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


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_name',)

class CourseListSerializer(serializers.ModelSerializer):
    degreee = serializers.StringRelatedField()
    class Meta:
        model = Course
        fields = '__all__'

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('institution_name',)

class InstitutionListSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    courses = serializers.StringRelatedField()
    class Meta:
        model = Institution
        fields = '__all__'


