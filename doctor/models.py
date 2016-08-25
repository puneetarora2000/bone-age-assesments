from __future__ import unicode_literals
from django.db import models
from time import time
from time import time
import random
import string

# Create your models here.

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)



class InsuranceCompany(models.Model):
	  InsuranceCompanyName = models.CharField(max_length=300)

class Patient(models.Model):
	Patient_ID = models.TextField(max_length=254)
	FullName = models.CharField(max_length=300)
	FullAddress= models.TextField(max_length=254)
	Patient_History = models.TextField()
	RegisterPatientRemoteMonitoring = models.BooleanField()
	Credential = models.FileField(upload_to = get_upload_file_name)
	Doctor_Visited_Id = models.TextField(max_length=254)
	InsuranceCompanyID = models.ForeignKey('InsuranceCompany',default=1,blank=True)


	def __unicode__(self):
		return self.Patient_ID

class RegisterDevicesForPatient(models.Model):
	Patient_ID = models.ForeignKey('Patient',default=1,blank=True)
	SugarMonitoringDevice = models.BooleanField(default=True)
	WorkOutMachineDevice = models.BooleanField(default=True)
	PulseMonitor = models.BooleanField(default=True)
	TemperatureMonitor =  models.BooleanField(default=True)
	SleepPatternsMonitor = models.BooleanField(default=True)
	GulcoseMonitoringDeviceID = models.CharField(max_length=200)
	WorkOutMachineDeviceID = models.CharField(max_length=200)
	PulseMonitorID = models.CharField(max_length=200)
	TemperatureMonitorID = models.CharField(max_length=200)
	SleepPatternsDeviceID =models.CharField(max_length=200)

	def __unicode__(self):
		return str(self.Patient_ID)


	def save(self,*args,**kwargs):
		random1 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
		self.GulcoseMonitoringDeviceID = 'GM' + str(self.Patient_ID) + random1
		random2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
		self.WorkOutMachineDeviceID = 'WM' + str(self.Patient_ID) + random2
		random3 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
		self.PulseMonitorID = 'PM' + str(self.Patient_ID) + random3
		random4 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
		self.TemperatureMonitorTM = 'TM' + str(self.Patient_ID) + random4
		random5 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
		self.SleepPatternsDeviceID  = 'SPM' + str(self.Patient_ID) + random5
		super(RegisterDevicesForPatient, self).save(*args, **kwargs)



class PatientHealthData(models.Model):
	Patient_ID = models.ForeignKey('Patient',default=1,blank=True)
	InsuranceCompanyID = models.ForeignKey('InsuranceCompany',default=1,blank=True)
	DataOfReading = models.DateTimeField(auto_now_add=True)
	SugarMonitoringDeviceReading = models.FloatField(default=0)
	WorkOutMachineDeviceReading = models.FloatField(default=0)
	PulseMonitorReading = models.FloatField(default=0)
	TemperatureMonitorReading =  models.FloatField(default=0)
	SleepPatternsMonitorReading = models.FloatField(default=0)
	def __unicode__(self):
		return self.Patient_ID