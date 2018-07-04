import os, csv, re

dirpath = os.getcwd()
csvpath = os.path.join(dirpath, 'filename.csv')
f=open(csvpath,'wb+')
f.truncate()
w=csv.writer(f)
for path, dirs, files in os.walk(dirpath):
    foo = re.compile(r'[A-Z]\d{2}[-]\d{4}', re.I)
    for filename in files:
        if foo.match(filename):
            part = filename[:-4]
            #print part + ' rev:' + rev
        #print(filename)
            w.writerow([part])
f.close()
#input()