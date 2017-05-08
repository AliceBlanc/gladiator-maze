import sys


def creerCase(mur, passage, sortie, joueur, gladiateur):
    case = {"mur": mur, "passage": passage, "sortie": sortie, "joueur": joueur, "gladiateur": gladiateur}
    return case


# def saisirCase():
#     nature = input("Quelle est la nature de la case ? (mur, passage, sortie ou rien)").lower()
#     if nature == "mur":
#         case = creerCase(True, False, False, False, False)
#     elif nature == "passage":
#         case = creerCase(False, True, False, False, False)
#     elif nature == "sortie":
#         case = creerCase(False, False, True, False, False)
#     else:
#         personnage = input("Quel personnage est sur la case ? (joueur,  gladiateur,  aucun)").lower()
#         if personnage == "joueur":
#             case = creerCase(False, False, False, True, False)
#         elif personnage == "gladiateur":
#             case = creerCase(False, False, False, False, True)
#         else:
#             case = creerCase(False, False, False, False, False)
#     return case


# def creerLabyrinthe(m, n):
#     labyrinthe = []
#     for i in range(0, m+1):
#         print(i)
#         liste = []
#         for j in range(0, n+1):
#             print(j)
#             case = saisirCase()
#             liste.append(case)
#         labyrinthe.append(liste)
#     return labyrinthe


def decodeLigne(chaine):
    ligne = []
    for c in chaine:
        if c == " ":
            ligne.append(creerCase(False, False, False, False, False))
        if c == "m":
            ligne.append(creerCase(True, False, False, False, False))
        if c == "p":
            ligne.append(creerCase(False, True, False, False, False))
        if c == "s":
            ligne.append(creerCase(False, False, True, False, False))
        if c == "j":
            ligne.append(creerCase(False, False, False, True, False))
        if c == "g":
            ligne.append(creerCase(False, False, False, False, True))
    return ligne


def lireDescription():
    labyrinthe = []
    x = int(input("Taille X du labyrinthe :"))
    # y = input("Taille Y du labyrinthe :")
    for a in range(0, 2 * x + 1):
        ligne = input("Ligne :")
        labyrinthe.append(decodeLigne(ligne))
    return labyrinthe


def lireFichier(fic):
    labyrinthe = []
    lignes = [line.rstrip('\n') for line in open(fic)]
    for l in lignes:
        labyrinthe.append(decodeLigne(l))
    return labyrinthe


def afficherLabyrinthe(lab):
    for lignes in lab:
        for case in lignes:
            if case['mur']:
                sys.stdout.write(chr(9608))
            elif case['passage']:
                sys.stdout.write(chr(9617))
            elif case['sortie']:
                sys.stdout.write(chr(9617))
            elif case['joueur']:
                sys.stdout.write(chr(9786))
            elif case['gladiateur']:
                sys.stdout.write(chr(9937))
            else:
                sys.stdout.write(' ')
        sys.stdout.write("\n")


def main():
    print('Lab : ', sys.argv[1])
    labyrinthe = lireFichier(sys.argv[1])
    afficherLabyrinthe(labyrinthe)


main()
