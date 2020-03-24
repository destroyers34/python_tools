# -*- coding: utf-8 -*-
import os
from shutil import copy2


drawing_dir = u"I:\\4-CONCEPTION\\4300-PIECES\\PE\\PDF\\"  # Doit se terminer par \\
currentfolder = os.path.dirname(os.path.abspath(__file__))

srcpath = drawing_dir
destpath = currentfolder


def get_revision(part):
    filelist = []
    listepiece = []
    fichier = ""
    for filename in os.listdir(drawing_dir):
        base, extension = os.path.splitext(filename)
        if filename.startswith(part) and extension.upper() == '.PDF':
            filelist.append(filename)
        else:
            continue
    print(filelist)
    log.write('Liste des PE trouver: ')
    for file in filelist:
        piece = file.replace('.', '_').split('_')
        if piece[1].startswith('T'):
            piece.insert(2, str(int(piece[1][1:]) + 0.1))
        else:
            piece.insert(2, str(int(piece[1]) * 10))
        listepiece.append(piece)
        log.write('\n')
        log.write(str(piece))
    log.write('\n')
    if len(listepiece) > 0:
        piece = max(listepiece, key=lambda x: x[2])
        fichier = piece[0] + '_' + piece[1] + ".PDF"
        log.write('Révision la plus récente: ' + str(fichier))
        log.write('\n')
    else:
        log.write('Aucun dessin trouver pour:' + str(fichier))
    return fichier
    #else:
        #log.write(str("ERREUR - DOSSIER INEXSISTANT: " + part))
        #log.write('\n')
        #return False


def getPartsList():
    with open('partslist.txt') as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        return content


partslist = getPartsList()
# print partslist
with open("log.txt", "w") as log:
    for part in partslist:
        revision = get_revision(part)
        if (revision):
            if part:
                if os.path.isfile((drawing_dir + revision)):
                    copy2((drawing_dir + revision), destpath)
                else:
                    print(part + " n'existe pas!")
                    print(drawing_dir + revision)
                    log.write(str("ERREUR - " + part + " n'existe pas!"))
                    log.write('\n')