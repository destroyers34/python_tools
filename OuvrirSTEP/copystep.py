# -*- coding: utf-8 -*-
import os
from shutil import copy2
import famillelist

currentfolder = os.path.dirname(os.path.abspath(__file__))
exec(compile(source=open(currentfolder + '\\famillelist.py').read(), filename='famillelist.py', mode='exec'))

drawing_dir = u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE DÉFINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\PARTS\\".encode('windows-1252')
#print drawing_dir

file_format = "STEP"

def getFamille(str):
	return famillelist[str[:3]]

def getRevision(part):
	#famille = getFamille(part)
	#print part.split('#')
	revSplit = part.split('_')
	#partSplit = part.split('#')
	#print revSplit[0]
	filelist = []
	file = ""
	for filename in os.listdir(drawing_dir):
		if filename.startswith(revSplit[0]) and filename.upper().endswith(file_format): 
			# print(os.path.join(directory, filename))
			filelist.append(filename)
			#continue
		else:
			continue
	#print filelist
	if len(filelist) > 0:
		print max(filelist)
	#log.write(str(filelist))
	#log.write('\n')
	if len(filelist) > 0:
		correction = max(filelist).split('_')
		correction = '_'.join(correction[:2]), '_'.join(correction[2:])
		file = correction[0]
		foundFile = file.split('.')[0].split('_')
		if len(revSplit)>1:
			if foundFile[1] != revSplit[1]:
				log.write(u'Asked for ' + str(revSplit) + u' but got ' + str(foundFile) + '\n')
		if file[-4:].upper() != 'STEP':
			file = file + '.STEP'
			#print file
			log.write(str(file))
			log.write('\n')
	else:
		log.write(str("ERREUR - FICHIER INEXSISTANT: " + (part)))
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
			partSplit = part.split('#')[0]
			if os.path.isfile((drawing_dir + "\\" + str(revision))):
				copy2((drawing_dir + "\\" + revision), currentfolder)
			else:
				print part + " n'existe pas!"
				print drawing_dir + "\\" + str(revision)
				log.write(str("ERREUR - " + partSplit + " n'existe pas!"))
				log.write('\n')
#raw_input("Appuyez sur une touche pour quitter")