from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from doctor.models import Patient,RegisterDevicesForPatient
from practitioner.models import Practitioner
from django.http import HttpResponse
from forms import PatientForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from doctor.serializers import GroupSerializer,PatientSerializer,UserSerializer,RegisterDevicesForPatientSerializer

# Create your views here.

def patients(request, doctor_id=1):
	args = {}
	args.update(csrf(request))
	args['doctor'] = doctor_id
	args['patients'] = Patient.objects.filter( Doctor_Visited_Id = doctor_id)
	return render_to_response('patients.html',
		args )


def patient(request, doctor_id=1 , patient_id=1):
	return render_to_response('patient.html', 
		{'patient': Patient.objects.get(id = patient_id), 'practitioner': Practitioner.objects.get(id = doctor_id)})


def create(request, doctor_id=1):
	if request.POST:
		form = PatientForm(request.POST, request.FILES)
		form.instance.Doctor_Visited_Id = doctor_id
		if form.is_valid():
			form.save()
			args = {}
			args['patients'] = Patient.objects.filter( Doctor_Visited_Id = doctor_id)
			return render_to_response('patients.html', args)

	else:
		form = PatientForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['doctor'] = doctor_id
	return render_to_response('create_patient.html', args)

#1
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
#2
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#7
class  PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
#7
class  RegisterDevicesForPatientViewSet(viewsets.ModelViewSet):
    queryset = RegisterDevicesForPatient.objects.all()
    serializer_class = RegisterDevicesForPatientSerializer



