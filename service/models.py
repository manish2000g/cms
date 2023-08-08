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
    description = models.TextField()
    test_type = models.CharField(max_length=10, choices=TEST_CHOICES)
    duration = models.PositiveIntegerField()  # Duration in days or weeks
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_capacity = models.PositiveIntegerField()
    schedule = models.CharField(max_length=255)  # E.g., Monday to Friday, 9:00 AM - 1:00 PM
    instructor = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    major_cities = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    visa_requirements = models.TextField(blank=True)

    def __str__(self):
        return self.name
  

class Course(models.Model):
    COURSE_TYPE_CHOICES = (
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Short Course', 'Short Course'),
    )

    name = models.CharField(max_length=255)
    description = RichTextField()
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    application_deadline = models.DateField()
    course_website = models.URLField(max_length=200, blank=True)
    course_image = models.ImageField(upload_to='course_images/', blank=True)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # courses = models.ManyToManyField(Course, related_name='institutions')
    website = models.URLField(max_length=200, blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=150, blank=True)
    logo = models.ImageField(upload_to='institution_logos/', blank=True)

    def __str__(self):
        return self.name


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

class Commission(models.Model):
    INCOME_SOURCES = (
        ('Admission Commission', 'Admission Commission'),
        ('Visa Processing Commission', 'Visa Processing Commission'),
        ('Other', 'Other'),
    )

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    income_date = models.DateField()
    income_source = models.CharField(max_length=100, choices=INCOME_SOURCES, default='Other')
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)
    agent = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.income_source} from {self.institution.name} ({self.country.name})"