# -*- coding: utf-8 -*-
import os, re, shutil

drawing_dir = u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE D\u00C9FINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\PDF\\"
foo = re.compile(r'[A-Z]\d{2}[-]\d{4}[_]', re.I)
excluded_extensions = ['db']

with open("pdf_list.txt", "w") as f:
    exclude = set(['000 - A Classer','000 - Autres PDF'])
    for root, directories, filenames in os.walk(drawing_dir, topdown=True):
        directories[:] = [d for d in directories if d not in exclude]
        for filename in filenames: 
            fichier_extension = filename.split('.')
            if fichier_extension[1].lower() == 'pdf':
                if foo.match(filename):
                    part = fichier_extension[0].split('_')
                    #print filename
                    f.write(str(part[0]+'_'+part[1]+'\n'))
                else:
                    #print os.path.join(root,filename)
                    #print filename          
                    shutil.move(os.path.join(root, filename), os.path.join(drawing_dir, '000 - A Classer'))
                    print (filename + ' has been moved to 000 - A Classer')
            elif fichier_extension[1].lower() in excluded_extensions:
                continue
            else:
                print (os.path.join(root, filename))
                continue
print('------------TERMINER----------------')