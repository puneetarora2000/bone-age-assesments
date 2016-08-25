from django.contrib import admin
from doctor.models import Patient,RegisterDevicesForPatient
from django import forms




class DeviceRegistationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    search_fields = ['id']
    fields = ('Patient_ID','SugarMonitoringDevice','WorkOutMachineDevice','PulseMonitor','TemperatureMonitor','SleepPatternsMonitor')
    list_display = ('id', 'patient_name','SugarMonitoringDevice','WorkOutMachineDevice','PulseMonitor','TemperatureMonitor','SleepPatternsMonitor','SleepPatternsDeviceID')
    model = RegisterDevicesForPatient

    def patient_name(self, instance):
        return instance.Patient_ID.FullName
    list_per_page = 10




admin.site.register(Patient)
admin.site.register(RegisterDevicesForPatient,DeviceRegistationAdmin)