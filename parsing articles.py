import csv
from RISparser import config
from RISparser import readris

config.LIST_TYPE_TAGS.append('JO')
config.TAG_KEY_MAPPING['JO'] = 'journal'

config.LIST_TYPE_TAGS.append('BT')
config.TAG_KEY_MAPPING['BT'] = 'journal_title'

 
content = []
 
with open("Dscience.Ris", 'r') as f:
    entries = readris(f)
    for e in entries:
        for k in e.keys():
            if k not in ['authors', 'keywords', 'primary_title', 'year', 'abstract', 'url']:
                e.pop(k, None)
        content.append(e)
 
 
with open('myArticles93.csv', 'w') as f:
 
    writer = csv.DictWriter(f, fieldnames=['primary_title','authors', 'keywords', 'year', 'abstract', 'url'])
    writer.writeheader()
    for element in content:
        writer.writerow(element)
    print("success")
