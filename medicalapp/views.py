from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from medicalapp.models import Doctors, Patients
from medicalapp.forms import Patientsform, Doctorsform
import urllib
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView


# Create your views here.
class index(TemplateView):
    template_name = 'medicalapp/index.html'

class Patientsform(FormView):
    model = Patients
    template_name = 'medicalapp/patients_appointment.html'


    # return render_to_response('medicalapp/index.html', context_dict, context)
