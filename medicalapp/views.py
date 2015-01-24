from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from medicalapp.models import Doctors, Patients
from medicalapp.forms import Patientsform, Doctorsform
import urllib
from django.http import HttpResponseRedirect
from django.views.generic import ListView


# Create your views here.
class Patientslist(ListView):
    model = Patients
    template_name = 'medicalapp/index.html'


    # return render_to_response('medicalapp/index.html', context_dict, context)
