from django.db import models

from service.models import Country, Course, Institution

class Document(models.Model):
    title = models.CharField(max_length=75)
    file = models.FileField(upload_to='applicant_documents/')

    def __str__(self):
        return self.title

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
    image = models.ImageField(upload_to='applicant_images/', blank=True)
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
    ielts_score = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    toefl_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pte_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gre_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gmat_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sat_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    other_language = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    interested_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    interested_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    documents = models.ManyToManyField(Document)
    interested_institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Application of {self.full_name}"


class Payment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    description = models.CharField(max_length=45)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    action = models.CharField(max_length=255)
    due_date = models.DateField()

    class Meta:
        unique_together = ('applicant', 'description')

    def __str__(self):
        return f"Payment for {self.applicant.full_name}"


class Commission(models.Model):
    INCOME_SOURCES = (
        ('Admission Commission', 'Admission Commission'),
        ('Visa Processing Commission', 'Visa Processing Commission'),
        ('Other', 'Other'),
    )

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    income_date = models.DateField()
    income_source = models.CharField(max_length=200, choices=INCOME_SOURCES)
    total_installment = models.DecimalField(max_digits=10, decimal_places=2)
    unpaid_installment = models.DecimalField(max_digits=10, decimal_places=2)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.income_source} from {self.institution.name} ({self.country.name})"
