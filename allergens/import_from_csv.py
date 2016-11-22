import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'allergens.settings'
import logging as log

from csv import DictReader

import django
django.setup()

from allergen_types.models import AllergenType, AllergenClass

AllergenClass.objects.all().delete()
klasses = ["Бытовые", "Пыльцевые", "Животные", "Фрукты", "Семена", "Овощи"]
AllergenClass.objects.bulk_create([AllergenClass(id=i+1, name=name) for i, name in enumerate(klasses)])

AllergenType.objects.all().delete()
with open('AllerType.csv', encoding='cp1251') as file:
    reader = DictReader(file)
    allergen_types = []
    for row in reader:
        klass = AllergenClass.objects.filter(pk=row['AllergenClass']).first()
        allergen_types += [AllergenType(
            id=int(row['AllergenNumber']),
            name=row['AllergenName'], 
            short_name=row['ShortName'], 
            klass=klass)]
    AllergenType.objects.bulk_create(allergen_types)

from patients.models import Patient
from datetime import date

Patient.objects.all().delete()
with open('Patients.csv', encoding='cp1251') as file:
    reader = DictReader(file)
    patients = []
    for row in reader:
        day, month, year = (int(x) for x in row['DateReceiving'].split('.'))
        if row['LastName']=='':
            log.warn('Empty last name for %s', row['PatientNumber'])
            row['LastName']='!!{}!!'.format(row['PatientNumber'])
        patients += [Patient(
            id = row['PatientNumber'],
            last_name = row['LastName'],
            first_name = row['FirstName'],
            middle_name = row['MiddleName'],
            registration_date = date(year, month, day),
            years = row['Years'] or None ,
            months = row['Months'] or None,
            attending_doctor = row['Director'])]
    Patient.objects.bulk_create(patients)
    

Patient.analyzes.through.objects.all().delete()    
with open('Analyses.csv', encoding='cp1251') as file:
    reader = DictReader(file)
    analyzes = {}
    for row in reader:
        if row['Appendix']!='+':
            log.warn('Strange appendix for (%s, %s)', row['PatientNumber'], row['AllergenNumber'])
        if row['OD']!='':
            log.warn('Strange OD for (%s, %s)', row['PatientNumber'], row['AllergenNumber'])
        allergen_type = AllergenType.objects.filter(pk=row['AllergenNumber']).first()
        patient = row['PatientNumber']
        if patient not in analyzes:
            analyzes[patient] = []
        analyzes[patient] += [allergen_type]
    for patient, a in analyzes.items():
        Patient.objects.filter(pk=patient).first().analyzes.add(*a)
