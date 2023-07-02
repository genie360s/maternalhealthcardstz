from django import forms

from regs.models import SpecialLaboratoryTests, ClinicalAttendance, MotherFirstVisit, MotherChildTransmission, PreviousPregnancyInformation

class ClinicalAttendanceForm(forms.ModelForm):   
    weight = forms.CharField(
        label="Weight (Kg)", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    blood_pressure = forms.CharField(
        label="Blood Pressure", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    albumin_in_urine = forms.ChoiceField(
        label="Albumin In Urine (+yes)/(-no)",
        choices=[
            ("+", "Yes"),
            ("-", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    blood_hb = forms.CharField(
        label="Blood/ Hb (8.5gm/d)", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    age_pregnancy_per_week = forms.CharField(
        label="Age Pregnancy Per Week", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    height_per_week = forms.CharField(
        label="Height Per Week", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    child_womb_position = forms.ChoiceField(
        label="Child's Womb Position",
        choices=[
            ("vertex", "Vertex or Head Down Position"),
            ("breech", "Breech Position"),
            ("transverse", "Transverse Position"),
            ("posterior", "Posterior Position"),
            ("anterior", "Anterior Position"),
            ("oa", "Occiput Anterior (OA) Position"),
            ("op", "Occiput Posterior (OP) Position")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    frontal_part_36th_week = forms.CharField(
        label="Frontal Part (36th Week)", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    child_moves_after_20th_week = forms.ChoiceField(
        label="Child Moves After 20th Week",
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    child_heartbeat_after_20th_week = forms.ChoiceField(
        label="Child Heart Beat After 20th Week",
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    swollen_legs_oedema = forms.ChoiceField(
        label="Swollen Legs (Oedema)(++)",
        choices=[
            ("+", "Yes"),
            ("-", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    ferrous_sulphate = forms.CharField(
        label="Ferrous Sulphate (2@day)", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    folic_acid = forms.ChoiceField(
        label="Folic Acid each day",
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    malaria_dose = forms.ChoiceField(
        label="MalariaDose(SP)(3pillsfro week-14)",
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    mebandozole = forms.CharField(
        label="Mebandozole(500 gm start)", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tetanus_vaccine = forms.ChoiceField(
        label="Tettanus Vaccine",
        choices=[
            ('0', 'Not Yet'),
            ('tt1', 'TT1'),
            ('tt2', 'TT2'),
            ('tt3', 'TT3'),
            ('tt4', 'TT4'),
            ('tt5', 'TT5')
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    dangerous_signs_symptoms = forms.ChoiceField(
        label="Dangerous Signs / Symptoms",
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    family_planning = forms.ChoiceField(
        label="Family Planning",
        choices=[
            ("1", "Yes"),
            ("0", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    delivery_preparations = forms.ChoiceField(
        label="Delivery Preparations",
        choices=[
            ("1", "Yes"),
            ("0", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    safe_sex_condom_usage = forms.ChoiceField(
        label="Safe Sex and Condom Usage",
        choices=[
            ("1", "Yes"),
            ("0", "No")
        ],
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )
    
    class Meta:
        model = ClinicalAttendance
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
     

class SpecialLaboratoryTestsForm(forms.ModelForm):
    

    class Meta:
        model = SpecialLaboratoryTests
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

        widgets = {
                'blood_group': forms.Select(attrs={'class': 'form-control form-select'}),
                'blood_rhesus_factor': forms.Select(attrs={'class': 'form-control form-select'}),
                'syphilis_sero_status': forms.Select(attrs={'class': 'form-control form-select'}),
                'blood_count': forms.TextInput(attrs={'class': 'form-control'}),
                'proteinuria': forms.TextInput(attrs={'class': 'form-control'}),
                'other_tests': forms.TextInput(attrs={'class': 'form-control'}),
            }
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class ObservationMotherFirstVisitForm(forms.ModelForm):

    class Meta:
        model = MotherFirstVisit
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

        widgets = {
                'age_below_20': forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'ten_years_or_more_since_last_birth': forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'c_section_operation' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'still_birth' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'fifth_pregnancy_or_more' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'height_below_150cm' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'c_section_or_vacuum_delivery' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'rectum_blockage' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'pregnancy_age_above_40' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'two_or_more_destructed_pregnancies' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'heart_disease' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'diabetes' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'tuberculosis' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'first_pregnancy_above_35' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'waist_disability' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'excess_bleeding_after_delivery' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                'mother_has_twins' : forms.CheckboxInput(attrs={'class': 'form-check-input fs-5'}),
                
            }
        

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class PreviousPregnanciesInformationForm(forms.ModelForm):

    class Meta:
        model = PreviousPregnancyInformation
        #fields = '__all__'
        exclude = ['created_at', 'updated_at']
        widgets = {
            'pregnancy_count': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_count': forms.TextInput(attrs={'class': 'form-control'}),
            'children_alive': forms.TextInput(attrs={'class': 'form-control'}),
            'bad_pregnancies': forms.TextInput(attrs={'class': 'form-control'}),
            'destructed_pregnancies_count': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_occurance': forms.TextInput(attrs={'class': 'form-control'}),
            'age_of_pregnancy': forms.TextInput(attrs={'class': 'form-control'}),
            'destruction_cause': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class MotherChildTransmissionForm(forms.ModelForm):

    class Meta:
        model = MotherChildTransmission
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

        widgets = {
            'pmtct_art' : forms.Select(attrs={'class': 'form-control form-select'}),
            'medicine_art' : forms.Select(attrs={'class': 'form-control form-select'}),
            'ctx_before_sickness_diagnosis' : forms.Select(attrs={'class': 'form-control form-select'}),
            'relation_with_ctc_service' : forms.Select(attrs={'class': 'form-control form-select'}),
            'child_food_diet' : forms.Select(attrs={'class': 'form-control form-select'}),
            'adherence' : forms.Select(attrs={'class': 'form-control form-select'}),
            'date_of_attendance' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'returning_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mc_personnel_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'mc_personnel_position' : forms.TextInput(attrs={'class': 'form-control'}),
            'comment_on_situation' : forms.Select(attrs={'class': 'form-control form-select'}),
            'mc_personnel_sign' : forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
