from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Pets(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length= 100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color_or_markings = models.CharField(max_length=100)
    birthday = models.DateField()
    
    sex_choices = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    sex = models.CharField(max_length=1, choices=sex_choices)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

class Parent(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    pets = models.ManyToManyField(Pets)
    created = models.DateTimeField(auto_now_add=True)
    occupation = models.CharField(max_length=100)
    contact_number =models.CharField(max_length =11)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Parent {self.first_name}"
    
class MedicalHistory(models.Model):
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    history_id = models.CharField(max_length=10, primary_key=True)
    chief_complaint = models.TextField()
    medication_given_prior_to_check_up = models.TextField()
    last_vaccination_given = models.CharField(max_length=100)
    last_vaccination_date = models.DateField(null =True)
    last_vaccination_brand = models.CharField(max_length=100)
    last_deworming_given = models.CharField(max_length=100)
    last_deworming_date = models.DateField(null =True)
    last_deworming_brand = models.CharField(max_length=100)
    is_transferred_from_other_clinic = models.BooleanField(default= False)
    name_of_clinic = models.CharField(max_length=100, blank=True, null=True)
    case = models.TextField(null=True)
    date_hospitalized = models.DateField(null=True)
    diet = models.TextField(null=True)
    weight = models.FloatField(null=True)
    initial_temp = models.FloatField(null=True)
    heart_rate = models.CharField(max_length = 100, null=True)
    respiratory_rate = models.CharField(max_length = 100, null=True)
    abnormal_findings = models.TextField(null=True)
    is_cbc = models.BooleanField(null=True)
    is_skin_scrape = models.BooleanField(null=True)
    is_xray = models.BooleanField(null=True)
    is_dfs = models.BooleanField(null=True)
    is_urinalysis = models.BooleanField(null=True)
    is_vaginal_smear = models.BooleanField(null=True)
    tentative_diagnosis = models.TextField(null=True)
    prognosis = models.TextField(null=True)
    treatment_given = models.TextField(null=True)
    take_home_meds = models.TextField(null=True)
    recommendations = models.TextField(null=True)
    followup_checkup_date = models.DateField(null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"MedicalHistory for {self.pet_id}"
    
class CustomUser(AbstractUser):
    name = models.CharField(max_length =100)
    username = models.CharField(max_length =100, unique = True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username' 
    