import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'allergens.settings'

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
        allergen_types += [AllergenType(id=int(row['AllergenNumber']),
            name=row['AllergenName'], 
            short_name=row['ShortName'], 
            klass=klass)]
    AllergenType.objects.bulk_create(allergen_types)
