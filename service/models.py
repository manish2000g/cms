from django.db import models
from ckeditor.fields import RichTextField
from account.models import UserProfile

class Service(models.Model):
    SERVICE_CHOICES = (
    ('Counseling', 'Counseling'),
    ('Visa Processing', 'Visa Processing'),
    ('Admission Assistance', 'Admission Assistance'),
    ('Scholarship Guidance', 'Scholarship Guidance'),
    ('Test Preparation', 'Test Preparation'),
    ('Document Verification', 'Document Verification'),
    ('Interview Preparation', 'Interview Preparation'),
    ('Application Review', 'Application Review'),
    ('Career Counseling', 'Career Counseling'),
  )
    name = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ClassSchedule(models.Model):
    test = models.CharField(max_length=10)
    class_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.PositiveIntegerField()
    max_capacity = models.PositiveIntegerField()
    instructor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.test 


class Test(models.Model):
    test_type = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='test_type')
    description = models.TextField()
    test_date = models.DateField()
    test_time = models.TimeField()
    max_capacity = models.PositiveIntegerField()
    result_date = models.DateField()

    def __str__(self):
        return f"{self.test_type.test} Test for {self.test_type.class_name}"


class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.country_name
  
class CourseType(models.Model):
    course_type = models.CharField(max_length=100)
    def __str__(self):
        return self.course_type


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    degree = models.ForeignKey(CourseType, on_delete=models.CASCADE, related_name='degree')
    description = RichTextField(blank=True)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    application_deadline = models.DateField()
    # course_image = models.ImageField(upload_to='course_images/', blank=True)

    def __str__(self):
        return self.course_name

class Institution(models.Model):
    institution_name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    courses = models.ManyToManyField(Course, related_name='courses')
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    # logo = models.ImageField(upload_to='institution_logos/', blank=True)

    def __str__(self):
        return self.institution_name


class Enquiry(models.Model):
    ENQUIRY_TYPES = (
        ('General', 'General Inquiry'),
        ('Visa', 'Visa Inquiry'),
        ('Course', 'Course Inquiry'),
    )

    ENQUIRY_STATUS_CHOICES = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_country = models.CharField(max_length=100)
    preferred_course = models.CharField(max_length=255)
    date_of_enquiry = models.DateField()
    enquiry_type = models.CharField(max_length=20, choices=ENQUIRY_TYPES)
    enquiry_status = models.CharField(max_length=20, choices=ENQUIRY_STATUS_CHOICES, default='Open')
    preferred_institution = models.CharField(max_length=200, blank=True, null=True)
    enquiry_assigned_to = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Enquiry from {self.name}"


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Event(models.Model):
    status_choices = (
        ('Upcoming', 'Upcoming'),
        ('Ongoing', 'Ongoing'),
        ('Past', 'Past'),
    )
    name = models.CharField(max_length=255)
    description = RichTextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    event_status = models.CharField(max_length=15, choices=status_choices, default='Upcoming')
    # tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.name

