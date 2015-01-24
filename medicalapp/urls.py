from django.conf.urls import patterns, include, url
from django.contrib import admin
from medicalapp.views import index,



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medicalrec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index.as_view()),
    url(r'^register/', Patientsform.as_view()),

)
