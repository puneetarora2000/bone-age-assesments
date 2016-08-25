from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	url(r'(?P<doctor_id>\d+)/all/$', 'doctor.views.patients'),
	url(r'(?P<doctor_id>\d+)/get/(?P<patient_id>\d+)/$', 'doctor.views.patient'),
	url(r'(?P<doctor_id>\d+)/create/$', 'doctor.views.create'),
	
	)