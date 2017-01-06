from django.shortcuts import render
from patients.models import Patient

plate = {'horizontal_indices': ['A','B','C','D','E','F','G','H'], 
         'vertical_indices': [1,2,3,4,5,6,7,8,9,10,11,12]}

def analyzes(request):
    context = {'patients': Patient.objects.all(), 'plate':plate }
    return render(request, 'analyzes/dashboard2.html', context)
