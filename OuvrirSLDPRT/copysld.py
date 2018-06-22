# -*- coding: utf-8 -*-
import os
from shutil import copy2

currentfolder = os.path.dirname(os.path.abspath(__file__))
exec(compile(source=open(currentfolder + '\\famillelist.py').read(), filename='famillelist.py', mode='exec'))

drawing_dir = u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE D\u00C9FINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\PARTS\\"
#print drawing_dir


def getFamille(str):
	return famillelist[str[:3]]

def getRevision(part):
	famille = getFamille(part)
	filelist = []
	for filename in os.listdir((drawing_dir)):
		if filename.startswith(part): 
			# print(os.path.join(directory, filename))
			#print filename
			filelist.append(filename)
			continue
		else:
			continue
	print filelist
	#print max(filelist)
	log.write(str(filelist))
	log.write('\n')
	correction = max(filelist).split('_')
	correction = '_'.join(correction[:2]), '_'.join(correction[2:])
	file = correction[0]
	if file[-6:].upper() != 'SLDPRT':
		file = file + '.SLDPRT'
	print file
	log.write(str(file))
	log.write('\n')
	return file
	
def getPartsList():
	with open('partslist.txt') as f:
		content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
		content = [x.strip() for x in content]
		return content
	

partslist = getPartsList()
#print partslist
with open("log.txt", "w") as log:			
	for part in partslist:
		revision = getRevision(part)
		#famille = getFamille(part)
		#currentfolder = os.path.dirname(os.path.abspath(__file__))
		if part:
	#		os.startfile((drawing_dir + famille + "\\" + part))
			if os.path.isfile((drawing_dir + "\\" + revision)):
				copy2((drawing_dir + "\\" + revision), currentfolder)
			else:
				print part + " n'existe pas!"
				print drawing_dir + "\\" + revision
				log.write(str(part + " n'existe pas!"))
				log.write('\n')
#raw_input("Appuyez sur une touche pour quitter")