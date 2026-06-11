from dronecmds import *
import traceback

def monprogramme():

    try:
        # ---------- PARAMÈTRES DE SÉCURITÉ -------
        marge = 50      # distance au mur (cm)
        pas = 50        # pas de déplacement (cm)

        # ---------- DIMENSIONS UTILES ----------
        large_utile = LARGE_SALLE - 2 * marge
        long_utile = LONG_SALLE - 2 * marge
        hauteur_utile = HAUTEUR_SALLE - 2 * marge

        # ---------- CALCUL DU MAILLAGE ----------
        nb_lignes = int(large_utile // pas)

        nb_couches = int(hauteur_utile // pas)

        # ---------- INITIALISATION ----------
        locate(x=marge, y=marge, heading=90)
        takeOff()
        goUp(marge)

        # ---------- PARCOURS 3D ----------
        for couche in range(nb_couches): 

            for ligne in range(nb_lignes):

                distance_y = 0
                while distance_y < long_utile:
                    forward(pas)
                    distance_y += pas

        # Détection de la cible

                    if isTargetDetected():
                        print("la Cible a été détectée")
                        land()
                        return

        # Demi-tour + décalage latéral

                if ligne < nb_lignes - 1:
                    if ligne % 2 == 0:
                        rotateRight(90)
                        forward(pas)
                        rotateRight(90)
                    else:
                        rotateLeft(90)
                        forward(pas)
                        rotateLeft(90)

        # Passage à la couche supérieure

            if couche < nb_couches - 1:
                goUp(pas)
                rotateRight(180)               # repositionnement pour nouvelle couche

        print("la Cible n'a pas été trouvée")
        land()

    except Exception as err:
        print(err)
        display()
        traceback.print_exc()


# ===================== PROGRAMME PRINCIPAL =====================
if __name__ == '__main__':

    print("=== Création de la salle ===")
    LARGE_SALLE = int(input("Donner la largeur de la salle (en cm) : "))
    LONG_SALLE = int(input("donner la longueur de la salle (en cm) : "))
    HAUTEUR_SALLE =int(input("donner la hauteur de la salle (en cm) : "))

    room_str = f"(0 0, {LARGE_SALLE} 0, {LARGE_SALLE} {LONG_SALLE}, 0 {LONG_SALLE}, 0 0)"
    createRoom(room_str, HAUTEUR_SALLE)

    print("\n=== Zone de génération de la cible ===")
    x1 = int(input("Entrer la valeur minimal de la position de la cible sur l'axe  X : "))
    x2 = int(input("Entrer la valeur maximal de la position de la cible sur l'axe  X :  "))
    y1 = int(input("Entrer la valeur minimal de la position de la cible sur l'axe  Y : "))
    y2 = int(input("Entrer la valeur maximal de la position de la cible sur l'axe  Y : "))
    z1 = int(input("Entrer la valeur minimal de la hauteur de la cible : "))
    z2 = int(input("Entrer la valeur maximale de la hauteur de la cible :"))

    createTargetIn(x1, y1, z1, x2, y2, z2)
    createDrone(DRONE_VIRTUAL, VIEWER_TKMPL, progfunc=monprogramme)

