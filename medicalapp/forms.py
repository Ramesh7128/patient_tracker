from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from medicalapp.models import Doctors, Patients


class Patientsform(forms.ModelForm):

    doctor = forms.ModelChoiceField(queryset=Doctors.objects.all())
    appointmentdate = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))

    class Meta:
        model = Patients
        fields = ('firstname', 'lastname', 'age', 'mobile', 'appointmentdate', 'doctor')

class Doctorsform(forms.ModelForm):

    class Meta:
        model = Doctors
        fields = ('firstname', 'lastname', 'specialisation')
