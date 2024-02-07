from django.db import models

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
    
class MedicalHistory(models.Model):
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    history_id = models.CharField(max_length=10, primary_key=True)
    chief_complaint = models.TextField()
    medication_given_prior_to_check_up = models.TextField()
    last_vaccination_given = models.CharField(max_length=100)
    last_vaccination_date = models.DateField()
    last_vaccination_brand = models.CharField(max_length=100)
    last_deworming_given = models.CharField(max_length=100)
    last_deworming_date = models.DateField()
    last_deworming_brand = models.CharField(max_length=100)
    is_transferred_from_other_clinic = models.BooleanField()
    name_of_clinic = models.CharField(max_length=100, blank=True, null=True)
    case = models.TextField()
    date_hospitalized = models.DateField()
    diet = models.TextField()
    weight = models.FloatField()
    initial_temp = models.FloatField()
    heart_rate = models.CharField(max_length = 100)
    respiratory_rate = models.CharField(max_length = 100)
    abnormal_findings = models.TextField()
    is_cbc = models.BooleanField()
    is_skin_scrape = models.BooleanField()
    is_xray = models.BooleanField()
    is_dfs = models.BooleanField()
    is_urinalysis = models.BooleanField()
    is_vaginal_smear = models.BooleanField()
    tentative_diagnosis = models.TextField()
    prognosis = models.TextField()
    treatment_given = models.TextField()
    take_home_meds = models.TextField()
    recommendations = models.TextField()
    followup_checkup_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"MedicalHistory for {self.pet_id}"
    