from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()

        }


#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    timing1 = forms.TimeInput(attrs={'type': 'time'})
    timing2 = forms.TimeInput(attrs={'type': 'time'})
    class Meta:
        model=models.Doctor
        widgets = {
            'timing1': forms.TimeInput(attrs={'type': 'time'}),
            'timing2': forms.TimeInput(attrs={'type': 'time'}),
        }
        fields=['address','mobile','department','status','profile_pic','timing1', 'timing2']

    def clean_timing1(self):
        timing1 = self.cleaned_data.get('timing1')
        return str(timing1)

    def clean_timing2(self):
        timing2 = self.cleaned_data.get('timing2')
        return str(timing2)



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    assignedDoctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all().filter(status=True),
        empty_label="Select a Doctor",
        to_field_name="user_id",  # Use the id field of the Doctor model as the value
    )

    # Override label_from_instance method to customize the display text
    def doctor_label_from_instance(self, doctor):
        timing1_str = doctor.timing1.strftime('%H:%M') if doctor.timing1 else 'N/A'
        timing2_str = doctor.timing2.strftime('%H:%M') if doctor.timing2 else 'N/A'
        return f"{doctor.get_name} ({doctor.department} - {timing1_str} to {timing2_str})"


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['assignedDoctorId'].label_from_instance = self.doctor_label_from_instance

    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    
    class Meta:
        model=models.Appointment
        fields=['description','status']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['name', 'email', 'message']

