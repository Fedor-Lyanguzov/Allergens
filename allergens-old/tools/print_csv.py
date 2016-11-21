from csv import DictReader

with open('AllerType.csv', encoding='cp1251') as file:
    reader = DictReader(file)
    for row in reader:
        print(row)
