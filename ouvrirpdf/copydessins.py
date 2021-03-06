# -*- coding: utf-8 -*-
import os
import re
import winshell
import sys
from shutil import copy2

sys.path.insert(0, "C:\\Users\\abechard\\PycharmProjects\\python_tools")
from variables.famillelist import familles

currentfolder = os.path.dirname(os.path.abspath(__file__))
step_dir = "I:\\4-CONCEPTION\\4300-PIECES\\DEFINITION\\PARTS\\"  # Doit toujours se terminer par \\
pdf_dir = "I:\\4-CONCEPTION\\4300-PIECES\\DEFINITION\\PDF\\"  # Doit toujours se terminer par \\
drawing_dir = "I:\\4-CONCEPTION\\4300-PIECES\\DEFINITION\\PDF\\"  # Doit toujours se terminer par \\
file_format = '.PDF'

def get_famille(texte):
    try:
        return familles[texte[:3]]
    except:
        log.write(texte[:3] + " - famille de pièce inconnu")
        log.write('\n')
        return ''


def get_revision(part):
    famille = get_famille(part)
    #print (get_famille(part))
    filelist = []
    listepiece = []
    fichier = ""
    if choix_format == '2':
        path = famille + "\\" + part
    else:
        path = ''
    #print(drawing_dir + path)
    if famille:
        if os.path.isdir((drawing_dir + path)):
            for filename in os.listdir((drawing_dir + path)):
                base, extension = os.path.splitext(filename)
                # print(filename)
                # print(filename.startswith(part))
                # print(extension.upper() == file_format)
                if filename.startswith(part) and extension.upper() == file_format:
                    # print(os.path.join(directory, filename))
                    # print (filename[-3:].upper())
                    filelist.append(filename)
                else:
                    continue
            print(filelist)
            log.write('Liste des pièces trouver: ')
            for file in filelist:
                piece = file.replace('.', '_').split('_')
                #print(piece)
                if piece[1][-1:] == "W":
                    piece[1] = piece[1][:-1]
                if piece[1].startswith('T'):
                    piece.insert(2, str(int(piece[1][1:]) + 0.1))
                else:
                    piece.insert(2, str(int(piece[1][:2]) * 10))
                listepiece.append(piece)
                log.write('\n')
                log.write(str(piece))
                # print (piece)
            # print (max(listepiece, key=lambda x: x[3]))
            log.write('\n')
            if len(listepiece) > 0:
                piece = max(listepiece, key=lambda x: x[2])
                fichier = piece[0] + '_' + piece[1]
                # correction = max(filelist).split('_')
                # correction = '_'.join(correction[:2]), '_'.join(correction[2:])
                # fichier = correction[0]
                # if fichier[-3:].upper() != 'PDF':
                #    fichier = fichier + '.PDF'
                # print (fichier)
                log.write('Révision la plus récente: ' + str(fichier))
                log.write('\n')
            else:
                log.write('Aucun dessin trouver pour:' + str(fichier))
            return fichier
        else:
            log.write(str("ERREUR - DOSSIER INEXSISTANT: " + path))
            log.write('\n')
            return False
    else:
        return False


def get_parts_list():
    with open('partslist.txt', 'r', encoding='utf-8') as f:
        regex = re.compile(u'[A-Za-z]\d{2}[-]\d{4}', re.I)
        partlist = f.readlines()
        string = ''.join(partlist).upper()
        partlist = re.findall(regex, string)
        return partlist


partslist = get_parts_list()
#print(partslist)
with open("log.txt", "w") as log:
    choix_format = input('Choisir le format: [1].STEP, [2].PDF, [3].SLDPRT\n').upper()
    #choix_format = ''
    if choix_format == '1':
        file_format = '.STEP'
        drawing_dir = step_dir
    elif choix_format == '2':
        file_format = '.PDF'
        drawing_dir = pdf_dir
    elif choix_format == '3':
        file_format = '.SLDPRT'
        drawing_dir = step_dir
    else:
        file_format = '.PDF'
        drawing_dir = pdf_dir
    choix = input('Choisir le mode: [C]opier, [R]accourci, [CR]Combine les deux \n').upper()
    for part in partslist:
        log.write('--------------------------------\n')
        log.write('Part: ' + part + '\n')
        revision = get_revision(part)
        if (revision):
            famille = get_famille(part)
            #			#currentfolder = os.path.dirname(os.path.abspath(__file__))
            if part:
                #		os.startfile((drawing_dir + famille + "\\" + part))
                if choix_format == '2':
                    cible = drawing_dir + famille + "\\" + part + "\\" + revision + file_format
                    #print(cible)
                else:
                    cible = drawing_dir + revision + file_format
                    #print(cible)
                if os.path.isfile(cible):
                    if choix == 'C':
                        copy2(cible, currentfolder)
                        log.write('Dessin copier: ' + revision)
                        log.write('\n')
                    elif choix == 'R':
                        # print cible
                        winshell.CreateShortcut(Path=os.path.join(currentfolder, revision + '.lnk'), Target=cible)
                    elif choix == 'CR':
                        copy2(cible, currentfolder)
                        log.write('Dessin copier: ' + revision)
                        log.write('\n')
                        winshell.CreateShortcut(Path=os.path.join(currentfolder, revision + '.lnk'), Target=cible)
                    else:
                        copy2(cible, currentfolder)
                        log.write('Dessin copier: ' + revision)
                        log.write('\n')
                else:
                    # print (part + " n'existe pas!")
                    # print (drawing_dir + famille + "\\" + part + "\\" + revision)
                    log.write(str("ERREUR - " + part + " n'existe pas!"))
                    log.write('\n')
                # input("Appuyez sur une touche pour quitter")
        log.write('--------------------------------\n')
