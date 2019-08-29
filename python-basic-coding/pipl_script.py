from pymongo import MongoClient
import csv
client = MongoClient("mongodb_path”)
emails = []
test=[]
with open(‘Path to file’,’r’) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
	    test.append(row)
for e in test:
    pipl = client.identity.pipl.find_one(e)
    print pipl
    try:
        email = pipl['email']
        pipl = pipl['pipl']
        print pipl
        if 'person' in pipl:
            person = pipl['person']
        elif 'possible_persons' in pipl:
            person = pipl['possible_persons'][0]
        else:
            person = None
        urls = ''
        if person:
            purls = person.get('urls', [])
            for url in purls:
                urls += (url['url'] + ',')
        with open('pipl_urls.csv', 'a') as pf:
            print 'hello'
            pf.write(email + ',' + urls + '\n')
    except:
        pass
