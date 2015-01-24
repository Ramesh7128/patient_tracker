from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from medicalapp.models import Doctors, Patients
from medicalapp.forms import Patientsform, Doctorsform
import urllib
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {}

    if request.method == "GET":
        form1 = Patientsform()
        form2 = Doctorsform()
        context_dict['form1'] = form1
        context_dict['form2'] = form2
    return render_to_response('medicalapp/index.html', context_dict, context)
