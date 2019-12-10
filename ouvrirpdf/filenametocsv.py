import os, csv, re

dirpath = u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE D\u00C9FINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\PDF\\"
csvpath = os.path.join(os.getcwd(), 'filename.csv')
f=open(csvpath,'w', newline='')
f.truncate()
w=csv.writer(f)
for path, dirs, files in os.walk(dirpath):
    foo = re.compile(r'[A-Z]\d{2}[-]\d{4}', re.I)
    for filename in files:
        if foo.match(filename):
            part = filename[:-4]
            #print (part)
        #print(filename)
            w.writerow([part])
f.close()
#input()