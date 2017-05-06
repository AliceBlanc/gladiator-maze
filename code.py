def creerCase(mur, passage, sortie, joueur, gladiateur):
    case = {"mur": mur, "passage": passage, "sortie": sortie, "joueur": joueur, "gladiateur": gladiateur}
    return case


def saisirCase():
    nature = input("Quelle est la nature de la case ? (mur, passage, sortie ou rien)").lower()
    if nature == "mur":
        case = creerCase(True, False, False, False, False)
    elif nature == "passage":
        case = creerCase(False, True, False, False, False)
    elif nature == "sortie":
        case = creerCase(False, False, True, False, False)
    else:
        personnage = input("Quel personnage est sur la case ? (joueur,  gladiateur,  aucun)").lower()
        if personnage == "joueur":
            case = creerCase(False, False, False, True, False)
        elif personnage == "gladiateur":
            case = creerCase(False, False, False, False, True)
        else:
            case = creerCase(False, False, False, False, False)
    return case


def creerLabyrinthe(m, n):
    labyrinthe = []
    for i in range(0, m+1):
        print(i)
        liste = []
        for j in range(0, n+1):
            print(j)
            case = saisirCase()
            liste.append(case)
        labyrinthe.append(liste)
    return labyrinthe


def main():
    labyrinthe = creerLabyrinthe(1, 1)
    print(labyrinthe)


main()
