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
    full_name = models.CharField(max_length=100, null=True)
    pets = models.ManyToManyField(Pets)
    created = models.DateTimeField(auto_now_add=True)
    occupation = models.CharField(max_length=100)
    contact_number =models.CharField(max_length =11)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Parent {self.name}"
    
class MedicalHistory(models.Model):
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    history_id = models.CharField(max_length=10, primary_key=True)
    chief_complaint = models.TextField( blank = True)
    medication_given_prior_to_check_up = models.TextField( blank = True)
    last_vaccination_given = models.CharField(max_length=100, blank = True)
    last_vaccination_date = models.DateField(null = True , blank = True)
    last_vaccination_brand = models.CharField(max_length=100, blank = True)
    last_deworming_given = models.CharField(max_length=100,  blank = True)
    last_deworming_date = models.DateField(null = True , blank =True)
    last_deworming_brand = models.CharField(max_length=100 ,  blank =True)
    is_transferred_from_other_clinic = models.BooleanField( default= False)
    name_of_clinic = models.CharField(max_length=100,  blank =True)
    case = models.TextField(  blank =True)
    date_hospitalized = models.DateField(null = True , blank = True)
    diet = models.TextField(  blank =True)
    weight = models.FloatField(null = True ,blank =True)
    initial_temp = models.FloatField( null = True,  blank =True)
    heart_rate = models.CharField(max_length = 100,  blank =True)
    respiratory_rate = models.CharField(max_length = 100, blank =True)
    abnormal_findings = models.TextField(  blank =True)
    is_cbc = models.BooleanField( default = False)
    is_skin_scrape = models.BooleanField( default = False)
    is_xray = models.BooleanField( default = False)
    is_dfs = models.BooleanField( default = False)
    is_urinalysis = models.BooleanField( default = False)
    is_vaginal_smear = models.BooleanField( default = False)
    tentative_diagnosis = models.TextField( blank =True)
    prognosis = models.TextField( blank =True)
    treatment_given = models.TextField( blank =True)
    take_home_meds = models.TextField(  blank =True)
    recommendations = models.TextField(  blank =True)
    followup_checkup_date = models.DateField(null = True , blank = True)
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
    