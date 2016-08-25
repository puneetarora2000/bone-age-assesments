from django import forms
from models import Patient


class PatientForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ('Patient_ID', 'Patient_History', 'Credential')