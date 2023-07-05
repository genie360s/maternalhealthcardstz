from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator




#  models here.


class PreviousPregnancyInformation(models.Model):

    card_no = models.AutoField(primary_key=True)
    pregnancy_count = models.PositiveIntegerField()
    birth_count = models.PositiveIntegerField()
    children_alive = models.PositiveIntegerField()
    bad_pregnancies = models.PositiveIntegerField()
    destructed_pregnancies_count = models.PositiveIntegerField()
    year_of_occurance = models.PositiveIntegerField()
    age_of_pregnancy = models.PositiveIntegerField()
    destruction_cause = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Patient Card {self.card_no}"


    
class MotherFirstVisit(models.Model):
    age_below_20 = models.BooleanField()
    ten_years_or_more_since_last_birth = models.BooleanField()
    c_section_operation = models.BooleanField()
    still_birth = models.BooleanField()
    fifth_pregnancy_or_more = models.BooleanField()
    height_below_150cm = models.BooleanField()
    c_section_or_vacuum_delivery = models.BooleanField()
    rectum_blockage = models.BooleanField()
    pregnancy_age_above_40 = models.BooleanField()
    two_or_more_destructed_pregnancies = models.BooleanField()
    heart_disease = models.BooleanField()
    diabetes = models.BooleanField()
    tuberculosis = models.BooleanField()
    first_pregnancy_above_35 = models.BooleanField()
    waist_disability = models.BooleanField()
    excess_bleeding_after_delivery = models.BooleanField()
    mother_has_twins = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mother First Visit {self.id}"

class SpecialLaboratoryTests(models.Model):
    BLOOD_GROUP_CHOICES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )

    BLOOD_RHESUS_CHOICES = (
        ('+', 'positive'),
        ('-', 'negative'),
    )

    SYPHILIS_SERO_CHOICES = (
        ('positive', 'positive'),
        ('negative', 'negative'),
    )

    labtest_id = models.BigAutoField(primary_key=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    blood_rhesus_factor = models.CharField(max_length=1, choices=BLOOD_RHESUS_CHOICES)
    syphilis_sero_status = models.CharField(max_length=10, choices=SYPHILIS_SERO_CHOICES)
    blood_count = models.CharField()
    proteinuria = models.CharField()
    other_tests = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" lab test {self.labtest_id}"
    
    

class ClinicalAttendance(models.Model):
    
    BLOOD_PRESSURE_PATTERN = r'^\d+/\d+$'  # Regular expression pattern for blood pressure validation
    ALBUMIN_CHOICES = [
        ('+', '+'),  # Albumin In Urine positive
        ('-', '-'),  # Albumin In Urine negative
    ]
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    TT_CHOICES = [
        ('0', 'Not Yet'),
        ('tt1', 'TT1'),
        ('tt2', 'TT2'),
        ('tt3', 'TT3'),
        ('tt4', 'TT4'),
        ('tt5', 'TT5'),
    ]

    weight = models.PositiveIntegerField(verbose_name="Weight (Kg)")
    blood_pressure = models.CharField(max_length=10, verbose_name="Blood Pressure",
                                      help_text="Format: Systolic/Diastolic (e.g., 120/80)",
                                      validators=[RegexValidator(regex=BLOOD_PRESSURE_PATTERN)])
    albumin_in_urine = models.CharField(max_length=1, choices=ALBUMIN_CHOICES, verbose_name="Albumin In Urine (+)")
    blood_hb = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Blood/Hb (8.5 gm/d)")
    age_pregnancy_per_week = models.PositiveIntegerField(verbose_name="Age Pregnancy Per Week")
    height_per_week = models.PositiveIntegerField(verbose_name="Height Per Week")
    child_womb_position = models.CharField(max_length=100, verbose_name="Child's Womb Position")
    frontal_part_36th_week = models.CharField(max_length=100, verbose_name="Frontal Part (36th Week)")
    child_moves_after_20th_week = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                   verbose_name="Child Moves After 20th Week")
    child_heartbeat_after_20th_week = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                       verbose_name="Child Heart Beat After 20th Week")
    swollen_legs_oedema = models.CharField(max_length=3, verbose_name="Swollen Legs (Oedema)(++)")
    ferrous_sulphate = models.PositiveIntegerField(verbose_name="Ferrous Sulphate (2@day)")
    folic_acid = models.CharField(max_length=3, choices=YES_NO_CHOICES, verbose_name="Folic Acid (1@day)")
    malaria_dose = models.CharField(max_length=3, choices=YES_NO_CHOICES, verbose_name="Malaria Dose (SP)(from wk-14)")
    mebandozole = models.CharField(max_length=100, verbose_name="Mebandozole (500 gm start)")
    tetanus_vaccine = models.CharField(max_length=4, choices=TT_CHOICES, verbose_name="Tetanus Vaccine")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at} {self.updated_at} attendance record"

class MotherChildTransmission(models.Model):
    PMTCT_ART_CHOICES = [
        (0, '0'),
        (-1, '-1'),
        (2, '2'),
    ]
    YES_NO_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
    ]
    MEDICINE_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
    ]
    FOOD_DIET_CHOICES = [
        ('MothersMilk', "Mother's Milk (EBF)"),
        ('AlternativeMilk', 'Alternative Milk (RF)'),
    ]
    ADHERENCE_CHOICES = [
        ('Good', 'Good'),
        ('Bad', 'Bad'),
    ]
    COMMENT_CHOICES = [
        ('Good', 'Good'),
        ('Bad (Critical)', 'Bad (Critical)'),
    ]

    pmtct_art = models.IntegerField(choices=PMTCT_ART_CHOICES, verbose_name="PMTCT / ART (0,-1,2)")
    medicine_art = models.CharField(max_length=3, choices=MEDICINE_CHOICES, verbose_name="Medicine (ART)")
    ctx_before_sickness_diagnosis = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                     verbose_name="CTX Before Sickness Diagnosis")
    relation_with_ctc_service = models.CharField(max_length=3, choices=YES_NO_CHOICES,
                                                 verbose_name="Relation with CTC Service")
    child_food_diet = models.CharField(max_length=15, choices=FOOD_DIET_CHOICES, verbose_name="Child's Food Diet")
    adherence = models.CharField(max_length=4, choices=ADHERENCE_CHOICES, verbose_name="Adherence")
    date_of_attendance = models.DateField(verbose_name="Date Of Attendance")
    returning_date = models.DateField(verbose_name="Returning Date")
    mc_personnel_name = models.CharField(max_length=100, verbose_name="Name of the MC Personnel")
    mc_personnel_position = models.CharField(max_length=100, verbose_name="Position of the MC Personnel")
    comment_on_situation = models.CharField(max_length=15, choices=COMMENT_CHOICES,
                                            verbose_name="Comment on the Situation")
    mc_personnel_sign = models.CharField(max_length=100, verbose_name="Sign of the MC Personnel")
    hospital_advised_to_deliver = models.CharField(max_length=100, verbose_name="Hospital Advised to Deliver", default="Muhimbili National Hospital")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at} mother child transmission record"

# delivery pain tables

# table 1

class Admission(models.Model):
    admission_id = models.BigAutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100, verbose_name="Admitted Hospital Name")
    admission_date = models.DateField(verbose_name="Admission Date")
    pain_begin_date = models.DateTimeField(verbose_name="Pain Begins")
    yoke_broke_date = models.DateTimeField(verbose_name="Yoke Broke")
    pregnancy_age_weeks = models.PositiveIntegerField(verbose_name="Age Of Pregnancy (Week)")
    pregnancy_height = models.FloatField(verbose_name="Height Of Pregnancy")
    womb_position = models.CharField(max_length=100, verbose_name="Child Womb Position")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital_name
    
    def __str__(self):
        return str(self.admission_id)
    
# table 2

class PelvicExam(models.Model):
    sacral_promontory = models.BooleanField(verbose_name="Sacral Promontory")
    ischial_spines_visible = models.BooleanField(verbose_name="Ischial Spines Visible")
    outlet_narrow = models.BooleanField(verbose_name="Outlet Narrow")
    pelvis_expansion = models.BooleanField(verbose_name="Pelvis Expansion")
    examiners_comments = models.TextField(verbose_name="Examiner's Comments")
    medical_personnel_name = models.CharField(max_length=100, verbose_name="Name of Medical Personnel")
    mc_personnel_position = models.CharField(max_length=100, verbose_name="Position of MC Personnel")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pelvic Exam #{self.pk}"
    
# table 3

class BirthComplications(models.Model):
    pregancy_age_hint_a_or_b = models.BooleanField(verbose_name="Hint A or B in Pregnancy Age (below 20 years)")
    yoke_broken_without_pain = models.BooleanField(verbose_name="Yoke Broken, Without Pain")
    birth_pain_before_34th_week = models.BooleanField(verbose_name="Birth Pain Before 34th Week")
    after_birth_pain_more_than_12hrs = models.BooleanField(verbose_name="More than 12hrs, After Birth Pain Started")
    wrong_child_position = models.BooleanField(verbose_name="Wrong Child Position")
    blood_ooze_on_birth_canal = models.BooleanField(verbose_name="Blood Ooze on the Birth Canal")
    change_of_child_heart_beats = models.BooleanField(verbose_name="Change of Child Heart Beats")
    fever_above_38c = models.BooleanField(verbose_name="Fever Above 38°C")
    placenta_blockage = models.BooleanField(verbose_name="Placenta Blockage")
    delivery_epilepsy_or_high_bp = models.BooleanField(verbose_name="Delivery Epilepsy / BP more than 140/90")
    blood_deficiency_below_8_5gmd = models.BooleanField(verbose_name="Blood Deficiency Below 8.5gm/d")
    placental_blockage_large_child_size = models.BooleanField(verbose_name="Placental Blockage / Large Child Size")
    meconium = models.BooleanField(verbose_name="Meconium")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Birth Complications #{self.pk}"
    
# table 4

class Delivery(models.Model):
    delivery_date = models.DateField(verbose_name="Delivery Date")
    delivery_type = models.CharField(max_length=100, verbose_name="Type Of Delivery")
    placenta_out_datetime = models.DateTimeField(verbose_name="Placenta Out (Date and Time)")
    c_section_performed = models.BooleanField(verbose_name="C-section Performed")
    reasons_for_c_section = models.TextField(verbose_name="Reasons For C-section")
    placenta_and_membrane_removed = models.BooleanField(verbose_name="Placenta and Membrane Fully Removed")
    blood_lost_ml = models.PositiveIntegerField(verbose_name="Blood Lost (ML)")
    ergometrine_or_oxytocin_induced = models.BooleanField(verbose_name="Ergometrine/Oxytocin Induced")
    tear_split = models.CharField(max_length=100, verbose_name="Split/Tear")
    medical_personnel_sewn_tear = models.CharField(max_length=100, verbose_name="Name of Medical Personnel Sewn Tear")
    mc_personnel_position = models.CharField(max_length=100, verbose_name="Position of MC Personnel")
    blood_pressure_after_delivery = models.CharField(max_length=100, verbose_name="Blood Pressure After Delivery")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery #{self.pk}"
    
# table 5

class DeliverySteps(models.Model):
    step_1_datetime = models.DateTimeField(verbose_name="Step 1 (Date and Time)")
    step_2_datetime = models.DateTimeField(verbose_name="Step 2 (Date and Time)")
    step_3_datetime = models.DateTimeField(verbose_name="Step 3 (Date and Time)")
    medical_personnel_delivered = models.CharField(max_length=100, verbose_name="Name of Medical Personnel Delivered")
    mc_personnel_signature = models.CharField(max_length=100, verbose_name="Signature of MC Personnel")
    further_delivery_comments = models.TextField(verbose_name="Further Delivery Comments")
    arvs_after_delivery = models.BooleanField(verbose_name="ARVs After Delivery")
    art_intake = models.BooleanField(verbose_name="ART Intake")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery Steps #{self.pk}"
    
# table 6

class Child(models.Model):
    WEIGHT_CHOICES = [(i, i) for i in range(1, 10)]
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    APGAR_CHOICES = [('1 minute', '1 minute'), ('5 minutes', '5 minutes')]
    NVP_CHOICES = [('1 week', '1 week'), ('4 weeks', '4 weeks')]
    NUTRITION_CHOICES = [('EBF', 'EBF'), ('RF', 'RF')]

    child_id = models.BigAutoField(primary_key=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Child's Weight")
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, verbose_name="Child's Sex")
    apgar_score = models.CharField(max_length=10, choices=APGAR_CHOICES, verbose_name="APGAR Score")
    arvs_intake = models.BooleanField(verbose_name="The Child has Intake of ARVs")
    nvp_dispensed = models.CharField(max_length=10, choices=NVP_CHOICES, verbose_name="NVP Dispensed")
    child_nutrition = models.CharField(max_length=10, choices=NUTRITION_CHOICES, verbose_name="Child's Nutrition")
    weight_below_2_5_kg = models.BooleanField(verbose_name="Weight below 2.5 kg")
    high_fever_above_38_degrees = models.BooleanField(verbose_name="High Fever Above 38°C")
    cant_suck_milk = models.BooleanField(verbose_name="Child Can't Suck Milk")
    apgar_score_5min_not_breathing = models.BooleanField(verbose_name="APGAR Score 5 minutes (Child not breathing)")
    child_physique_comments = models.TextField(verbose_name="Child Physique Observation: Comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Child #{self.pk}"
    
# publication

class ResearchPublication(models.Model):
    publication_no = models.BigAutoField(primary_key=True)
    authors = models.CharField(max_length=255, verbose_name="Name of Authors")
    publication_date = models.DateField(verbose_name="Date Of Publication")
    title = models.CharField(max_length=255, verbose_name="Research Title")
    description = models.TextField(verbose_name="Short Description")
    medical_field = models.CharField(max_length=100, verbose_name="Medical Field")
    article_file = models.FileField(upload_to="articles/", verbose_name="Upload Article")
    res_national_id = models.ForeignKey('accounts.Researcher', on_delete=models.CASCADE) # foreign key from researcher model

    def __str__(self):
        return self.titled
    
    def __str__(self):
        return str(self.publication_no)
# data request

class ResearchDataRequest(models.Model):
    DATA_FORMAT_CHOICES = [
        ('csv', 'CSV'),
        ('excel', 'Excel'),
    ]

    request_no = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Research Title")
    short_description = models.CharField(max_length=100, verbose_name="Short Title Description")
    data_description = models.TextField(verbose_name="Describe Data Requested")
    request_date = models.DateField(verbose_name="Date Of Request")
    data_format = models.CharField(max_length=10, choices=DATA_FORMAT_CHOICES, verbose_name="Choose Data Format")
    research_permit = models.FileField(upload_to="research_permits/", verbose_name="Upload Research Permit", help_text="Permit should be in PDF format")
    res_national_id = models.ForeignKey('accounts.Researcher', on_delete=models.CASCADE) # foreign key from researcher model

    def __str__(self):
        return self.title
    
    def __str__(self):
        return str(self.request_no)
    
