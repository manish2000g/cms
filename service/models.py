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
    TEST_CHOICES = (
        ('IELTS', 'IELTS'),
        ('PTE', 'PTE'),
        ('TOEFL', 'TOEFL'),
        ('DuoLingo', 'DuoLingo')
    )

    name = models.CharField(max_length=255)
    test_type = models.CharField(max_length=10, choices=TEST_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.PositiveIntegerField()
    max_capacity = models.PositiveIntegerField()
    instructor = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    description = models.TextField()
    test_date = models.DateField()
    test_time = models.TimeField()
    result_date = models.DateField()

    def __str__(self):
        return f"{self.class_schedule.test_type} Test for {self.class_schedule.name}"


class Country(models.Model):
    COUNTRY_CHOICES = (
        ('Australia', 'Australia'),
        ('Canada', 'Canada'),
        ('New Zealand', 'New Zealand'),
        ('USA', 'USA'),
        ('UK', 'UK'),
    )

    MAJOR_CITIES = (
        ('Sydney', 'Sydney'),
        ('Melbourne', 'Melbourne'),
        ('Brisbane', 'Brisbane'),
        ('Perth', 'Perth'),
        ('Adelaide', 'Adelaide'),
        ('Toronto', 'Toronto'),
        ('Vancouver', 'Vancouver'),
        ('Montreal', 'Montreal'),
        ('Calgary', 'Calgary'),
        ('Edmonton', 'Edmonton'),
        ('Auckland', 'Auckland'),
        ('Wellington', 'Wellington'),
        ('Christchurch', 'Christchurch'),
        ('Hamilton', 'Hamilton'),
        ('Queenstown', 'Queenstown'),
        ('New York City', 'New York City'),
        ('Los Angeles', 'Los Angeles'),
        ('Chicago', 'Chicago'),
        ('Houston', 'Houston'),
        ('San Francisco', 'San Francisco'),
        ('London', 'London'),
        ('Manchester', 'Manchester'),
        ('Birmingham', 'Birmingham'),
        ('Glasgow', 'Glasgow'),
        ('Edinburgh', 'Edinburgh'),
    )
    
    country_name = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    major_city = models.CharField(max_length=100, choices=MAJOR_CITIES)
    description = models.TextField(blank=True)
    visa_requirements = models.TextField(blank=True)

    def __str__(self):
        return self.country_name
  

class Course(models.Model):
    COURSE_TYPE_CHOICES = (
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Short Course', 'Short Course'),
    )

    course_name = models.CharField(max_length=255)
    description = RichTextField()
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    application_deadline = models.DateField()
    course_website = models.URLField(max_length=200, blank=True)
    course_image = models.ImageField(upload_to='course_images/', blank=True)

    def __str__(self):
        return self.course_name

class Institution(models.Model):
    institution_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='institutions')
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
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    status_choices = (
        ('Upcoming', 'Upcoming'),
        ('Ongoing', 'Ongoing'),
        ('Past', 'Past'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=status_choices, default='Upcoming')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

