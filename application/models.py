from django.db import models

class Applicant(models.Model):
    STATUS_CHOICES = (
        ('Interested', 'Interested'),
        ('Created', 'Created'),
        ('Submitted', 'Submitted'),
        ('Offer', 'Offer'),
        ('Visa Created', 'Visa Created'),
        ('Visa Submitted', 'Visa Submitted'),
        ('Docs Requested', 'Docs Requested'),
        ('Granted', 'Granted'),
        ('Rejected', 'Rejected'),
        ('Enrolled', 'Enrolled')
    )
    APPLICANT_PURPOSE_CHOICE =(
        ('Inquiring', 'Inquiring'),
        ('Class Enrollment', 'Class Enrollment'),
        ('Abroad Enrollment', 'Abroad Enrollment')
    )
    ACADEMIC_SCORE_CHOICE = (
        ('Percentage', 'Percentage'),
        ('GPA', 'GPA')
    )
    applicant_purpose = models.CharField(max_length=30, choices=APPLICANT_PURPOSE_CHOICE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Interested')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    dob = models.DateField()
    institution = models.CharField(max_length=200)
    degree_title = models.CharField(max_length=150)
    degree_level = models.CharField(max_length=50)
    passed_year = models.DateField()
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    academic_score_category = models.CharField(max_length=20, choices=ACADEMIC_SCORE_CHOICE)
    academic_score = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.CharField(max_length=150)    
    ielts_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    toefl_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    pte_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    gre_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    sat_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    other_language = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    interested_country = models.CharField(max_length=50)
    interested_course = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Application of {self.full_name}"


class EnglishProficiency(models.Model):
    TEST_CHOICES = (
        ('IELTS', 'IELTS'),
        ('PTE', 'PTE'),
        ('TOEFL', 'TOEFL')
    )
    student = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=10, choices=TEST_CHOICES)
    test_score = models.DecimalField(max_digits=5, decimal_places=2)
    test_date = models.DateField()

    def __str__(self):
        return f"{self.student.full_name}'s {self.test_name} - Score: {self.test_score}"

    