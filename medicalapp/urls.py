from django.conf.urls import patterns, include, url
from django.contrib import admin
from medicalapp.views import Patientslist



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medicalrec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Patientslist.as_view()),
)
