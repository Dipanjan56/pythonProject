from django.shortcuts import render
from . import models


# Create your views here.
def list_patients(request):
    all_patients = models.Patient.objects.all()
    context_patient = {'patients': all_patients}
    return render(request, 'dental_app/list.html', context=context_patient)
