from django.contrib.auth.models import User, Group
from doctor.models import  RegisterDevicesForPatient,Patient
from rest_framework import serializers



#1
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#2
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
#3
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Patient
        fields = ('Patient_ID','FullName','FullAddress','Patient_History','RegisterPatientRemoteMonitoring','Credential','Doctor_Visited_Id','InsuranceCompanyID')

#
class RegisterDevicesForPatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  RegisterDevicesForPatient
        fields = ('Patient_ID','SugarMonitoringDevice','WorkOutMachineDevice','PulseMonitor','TemperatureMonitor','SleepPatternsMonitor','GulcoseMonitoringDeviceID','WorkOutMachineDeviceID','PulseMonitorID','TemperatureMonitorID','SleepPatternsDeviceID')