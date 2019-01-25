# -*- coding: utf-8 -*-
import os, winshell, re
from shutil import copy2
#import famillelist

currentfolder = os.path.dirname(os.path.abspath(__file__))
#exec (compile(source=open('famillelist.py').read(), filename='famillelist.py', mode='exec'))
famillelist={
    'A01':'A01 - Adapter',
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
    'W03':'W03 - Wheel'
    }

drawing_dir = u"S:\\---ETI---NOMENCLATURE (NM)- PLANS D\'ENSSEMBLE (PE)-PLANS DE D\u00C9FINITIONS (X...)\\PLANS DE DEFINITION (X__-XXXX)\\PDF\\"
# print drawing_dir


def getFamille(texte):
    return famillelist[texte[:3]]


def getRevision(part):
    famille = getFamille(part)
    # print getFamille(part)
    filelist = []
    listepiece = []
    fichier = ""
    # print os.path.isdir((drawing_dir + famille + "\\" + part)).
    # print drawing_dir + famille + "\\" + part
    if os.path.isdir((drawing_dir + famille + "\\" + part)):
        for filename in os.listdir((drawing_dir + famille + "\\" + part)):
            if filename.startswith(part):
                # print(os.path.join(directory, filename))
                #print (filename[-3:].upper())
                if filename[-3:].upper() == 'PDF':
                    filelist.append(filename)
                continue
            else:
                continue
        #print (filelist)
        log.write('Liste des pièces trouver: ')
        for file in filelist:
            piece = file.replace('.','_').split('_')
            #print (piece)
            if piece[1].startswith('T'):
                piece.insert(2,str(int(piece[1][1:])+0.1))
            else:
                piece.insert(2,str(int(piece[1])*10)) 
            listepiece.append(piece)
            log.write('\n')
            log.write(str(piece))
            #print (piece)
        #print (max(listepiece, key=lambda x: x[3]))
        log.write('\n')
        piece = max(listepiece, key=lambda x: x[2])
        fichier = piece[0] + '_' + piece[1]
        #correction = max(filelist).split('_')
        #correction = '_'.join(correction[:2]), '_'.join(correction[2:])
        #fichier = correction[0]
        #if fichier[-3:].upper() != 'PDF':
        #    fichier = fichier + '.PDF'
        #print (fichier)
        log.write('Révision la plus récente: ' + str(fichier))
        log.write('\n')
        return fichier
    else:
        log.write(str("ERREUR - DOSSIER INEXSISTANT: " + (famille + "\\" + part)))
        log.write('\n')
        return False


def getPartsList():
    with open('partslist.txt') as f:
        content = f.readlines()
        # print content
        # raw_input()
        foo = re.compile(r'[A-Z]\d{2}[-]\d{4}', re.I)
        try:
            content = [re.findall(foo, x)[0] for x in content if x!="\n"]
        except IndexError:
            pass
        #for x in content:
            #print (x)
        #input()
        return content


partslist = getPartsList()
# print partslist
with open("log.txt", "w") as log:
    for part in partslist:
        log.write('--------------------------------\n')
        log.write('Part: ' + part + '\n')
        revision = getRevision(part)
        if (revision):
            famille = getFamille(part)
            #			#currentfolder = os.path.dirname(os.path.abspath(__file__))
            if part:
                #		os.startfile((drawing_dir + famille + "\\" + part))
                cible = drawing_dir + famille + "\\" + part + "\\" + revision + '.PDF'
                if os.path.isfile(cible):
                    copy2(cible, currentfolder)
                    log.write('Dessin copier: ' + revision)
                    log.write('\n')
                    # print cible
                    # winshell.CreateShortcut(Path=os.path.join (currentfolder, revision+'.lnk'),Target=cible)
                else:
                    #print (part + " n'existe pas!")
                    #print (drawing_dir + famille + "\\" + part + "\\" + revision)
                    log.write(str("ERREUR - " + part + " n'existe pas!"))
                    log.write('\n')
                #input("Appuyez sur une touche pour quitter")
        log.write('--------------------------------\n')