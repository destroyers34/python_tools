# -*- coding: utf-8 -*-
import os
import shutil
import ctypes
import Tkinter
import tkMessageBox
import time
import re

dt = time.strftime('%Y-%m-%d %H:%M:%S') + ': '

foo = re.compile(r'[A-Z]\d{2}[-]\d{4}[_]', re.I)

famillelist = { 'A01':'A01 - Adapter',
'A02':'A02 - Axle',
'A03':'A03 - Angle',
'A04':'A04 - Arm',
'B01':'B01 - Bushing',
'B02':'B02 - Beam',
'B03':'B03 - Bracket',
'B04':'B04 - Box',
'B05':'B05 - Block',
'B06':'B06 - Buffer',
'B07':'B07 - Bac',
'B08':'B08 - Bumper',
'B09':'B09 - Blade',
'B10':'B10 - Belt',
'B11':'B11 - Electric Box',
'C01':'C01 - Casing',
'C02':'C02 - Carriage',
'C03':'C03 - Cover',
'C04':'C04 - Clamp',
'C05':'C05 - Chute',
'C06':'C06 - Cap',
'C07':'C07 - Cam',
'C08':'C08 - Coupling',
'C09':'C09 - Channel',
'C10':'C10 - Collar',
'C11':'C11 - Cabinet',
'C12':'C12 - Caliper',
'C13':'C13 - Corner',
'C14':'C14 - Clutch',
'D01':'D01 - Door',
'D02':'D02 - Desk',
'D03':'D03 - Duct',
'F01':'F01 - Frame',
'F02':'F02 - Finger',
'F03':'F03 - Foot',
'G01':'G01 - Guard',
'G02':'G02 - Guide',
'G03':'G03 - Gear',
'G04':'G04 - Gauge',
'H01':'H01 - Hub',
'H02':'H02 - Handle',
'H03':'H03 - Hook',
'J01':'J01 - Jaw',
'K01':'K01 - Key',
'L01':'L01 - Lever',
'L02':'L02 - Lock',
'L03':'L03 - Levelling',
'M01':'M01 - Manifold',
'M02':'M02 - Mold',
'N01':'N01 - Nut',
'N02':'N02 - Nozzle',
'P01':'P01 - Plate',
'P02':'P02 - Pulley',
'P03':'P03 - Pin',
'P04':'P04 - Panel',
'P05':'P05 - Pan',
'P06':'P06 - Profil',
'P07':'P07 - Pillow Block',
'P08':'P08 - Pad',
'P09':'P09 - Plug',
'P10':'P10 - Plunger',
'P11':'P11 - Pedal',
'P12':'P12 - Pusher',
'P13':'P13 - Pallet',
'R01':'R01 - Rod',
'R02':'R02 - Rib',
'R03':'R03 - Ring',
'R04':'R04 - Roller',
'R05':'R05 - Rail',
'R06':'R06 - Ramp',
'R07':'R07 - Reinforcement',
'R08':'R08 - Rack',
'S01':'S01 - Shaft',
'S02':'S02 - Stopper',
'S03':'S03 - Skate',
'S04':'S04 - Spacer',
'S05':'S05 - Support',
'S06':'S06 - Slide',
'S07':'S07 - Screw',
'S08':'S08 - Side',
'S09':'S09 - Seal',
'S10':'S10 - Seat',
'S11':'S11 - Spring',
'S12':'S12 - Sticker',
'T01':'T01 - Tensioner',
'T02':'T02 - Table',
'T03':'T03 - Tole',
'T04':'T04 - Tray',
'T05':'T05 - Tool',
'T06':'T06 - Tip',
'T07':'T07 - Temporary Parts',
'W01':'W01 - Washer',
'W02':'W02 - Weight',
'W03':'W03 - Wheel'}

def getFamille(part):
	return famillelist[part[:3]]

def getRevision(part):
	famille = getFamille(part)
	filelist = []
	for filename in os.listdir((u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE D\u00C9FINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\PDF\\" + famille + "\\" + part)):
		if filename.startswith(part): 
			# print(os.path.join(directory, filename))
			#print filename
			filelist.append(filename)
			continue
		else:
			continue
	print (filelist)
	print (max(filelist))
	return (max(filelist))

#srcpath = 'C:\Users\\abechard\\Desktop\\test'
srcpath = os.path.dirname(os.path.abspath(__file__))
#destpath = 'C:\\Users\\abechard\\Desktop\\test'
destpath = u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE D\u00C9FINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\PDF"

#print srcpath
#print destpath

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

with open("log.txt", "a") as f:
	for root, subFolders, files in walklevel(srcpath, level=1):
		for file in files:
			#famille = file[-3:]
			if file[-3:].upper() == 'PDF':
				if foo.match(file):
					subFolder = os.path.join(destpath, getFamille(file[:3]), file[:8])
					#print subFolder
					#print file
					#print getFamille(file)
					if not os.path.isdir(subFolder):
						os.makedirs(subFolder)
						f.write(str(dt + "Created folder " + file + "\n"))
					#print os.path.join(root, file)
					if os.path.isfile(os.path.join(subFolder, file)):
						print (file[:11] + u" existe!")
						f.write(str(dt + file[:11] + u" existe!\n"))
						result = tkMessageBox.askquestion("Remplacer", (file[:11] + u" existe! Voulez-vous le remplacer?"), icon='warning')
						if result == 'yes':
							shutil.copy(os.path.join(root, file), subFolder)
							print (file[:11] + u" remplacer")
							f.write(str(dt + file[:11] + u" remplacer!\n"))
					else:
						shutil.move(os.path.join(root, file), subFolder)
						print ("Moved " + file)
						f.write(str(dt + "Moved " + file + "\n"))
						continue
				else:
					continue
			else:
				continue
	#raw_input("Appuyez sur une touche pour quitter")
	
