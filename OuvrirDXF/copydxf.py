# -*- coding: utf-8 -*-
import os
from shutil import copy2
import famillelist

currentfolder = os.path.dirname(os.path.abspath(__file__))
exec(compile(source=open(currentfolder + '\\famillelist.py').read(), filename='famillelist.py', mode='exec'))

drawing_dir = u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE D\u00C9FINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\DXF\\".encode('windows-1252')
#print drawing_dir

def getFamille(str):
	return famillelist[str[:3]]

def getRevision(part):
	famille = getFamille(part)
	#print part.split('#')
	partSplit = part.split('#')[0]
	#print partSplit
	filelist = []
	file = ""
	if os.path.isdir((drawing_dir + famille + "\\" + partSplit)):
		for filename in os.listdir((drawing_dir + famille + "\\" + partSplit)):
			if filename.startswith(part): 
				# print(os.path.join(directory, filename))
				#print filename
				filelist.append(filename)
				continue
			else:
				continue
		#print filelist
		if len(filelist) > 0:print max(filelist)
		#log.write(str(filelist))
		#log.write('\n')
		if len(filelist) > 0:
			correction = max(filelist).split('_')
			correction = '_'.join(correction[:2]), '_'.join(correction[2:])
			file = correction[0]
			if file[-3:].upper() != 'DXF':
				file = file + '.DXF'
				#print file
				log.write(str(file))
				log.write('\n')
		else:
			log.write(str("ERREUR - FICHIER INEXSISTANT: " + (drawing_dir + famille + "\\" + part)))
			log.write('\n')
		return file
	else:
		log.write(str("ERREUR - DOSSIER INEXSISTANT: " + (drawing_dir + famille + "\\" + partSplit)))
		log.write('\n')
		return False

	
def getPartsList():
	with open('partslist.txt') as f:
		content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
		content = [x.strip() for x in content]
		#print content
		return content
	

partslist = getPartsList()
#print partslist
with open("log.txt", "w") as log:			
	for part in partslist:
		revision = getRevision(part)
		if(revision):
			famille = getFamille(part)
			#currentfolder = os.path.dirname(os.path.abspath(__file__))
			if part:
		#		os.startfile((drawing_dir + famille + "\\" + part))
				partSplit = part.split('#')[0]
				if os.path.isfile((drawing_dir + famille + "\\" + partSplit + "\\" + revision)):
					copy2((drawing_dir + famille + "\\" + partSplit + "\\" + revision), currentfolder)
				else:
					print part + " n'existe pas!"
					print drawing_dir + famille + "\\" + partSplit + "\\" + revision
					log.write(str("ERREUR - " + partSplit + " n'existe pas!"))
					log.write('\n')
#raw_input("Appuyez sur une touche pour quitter")