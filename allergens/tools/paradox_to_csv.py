from pypxlib import Table
from csv import DictWriter
from glob import glob
from traceback import print_exc

names = glob('./*.db')
for name in names:
    table = Table(name, encoding='cp1251')
    try:
        with open(name[:-3]+'.csv', 'w', encoding='utf-8', newline='') as file:
            fields = [ a for a in table.fields if not a.startswith('Date')]
            writer = DictWriter(file, fields, extrasaction='ignore')
            writer.writeheader()
            for row in table:
                row2 = { key: row[key] for key in fields }
                writer.writerow(row2)
    except:
        print_exc()
    finally:
        table.close()
