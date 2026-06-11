#  Drone Explorer 3D : Recherche Autonome de Cible dans un Environnement Tridimensionnel

##  Présentation du projet

Ce projet a été réalisé dans le cadre d'un enseignement d'algorithmique et de programmation en Python. Il consiste à développer le comportement autonome d'un drone virtuel chargé d'explorer un environnement tridimensionnel afin de localiser une cible dont la position est inconnue.

Le drone évolue dans une salle fermée aux dimensions configurables et dispose d'un capteur de proximité lui permettant de détecter la cible uniquement lorsqu'il se trouve à moins de 50 cm de celle-ci. L'objectif principal est donc de concevoir un algorithme de navigation capable d'assurer une couverture complète de l'espace tout en respectant les contraintes de sécurité imposées par l'environnement.

---

##  Objectifs pédagogiques

Ce projet vise à mettre en pratique plusieurs notions fondamentales de l'algorithmique :

- Conception et implémentation d'algorithmes de recherche.
- Décomposition d'un problème complexe en sous-problèmes.
- Gestion des déplacements dans un espace tridimensionnel.
- Utilisation de structures itératives et conditionnelles.
- Gestion des exceptions et robustesse du programme.
- Modélisation d'un parcours optimisé.

---

##  Principe de fonctionnement

Le drone suit une stratégie d'exploration systématique reposant sur un balayage de l'espace :

1. Décollage et mise à altitude de sécurité.
2. Exploration de chaque ligne de la salle selon un parcours en zigzag.
3. Couverture complète de chaque couche horizontale.
4. Passage progressif aux couches de hauteur supérieures.
5. Vérification de la présence de la cible après chaque déplacement.
6. Atterrissage immédiat dès que la cible est détectée.
7. Arrêt du programme après exploration complète si aucune cible n'est trouvée.

Cette méthode garantit une couverture exhaustive de l'espace de recherche.

---

##  Architecture du projet
Projet Drone
│
├── Programme principal
│ ├── Création de la salle
│ ├── Génération de la cible
│ └── Initialisation du drone
│
├── Algorithme de navigation
│ ├── Décollage
│ ├── Parcours des lignes
│ ├── Parcours des couches
│ ├── Détection de cible
│ └── Atterrissage
│
└── Gestion des erreurs

---

##  Algorithme utilisé

L'exploration repose sur une stratégie de balayage tridimensionnel :

- Axe **Y** : déplacement longitudinal.
- Axe **X** : changement de ligne.
- Axe **Z** : changement de couche de hauteur.

Le drone parcourt chaque couche selon un mouvement en zigzag afin de minimiser les déplacements inutiles tout en assurant une couverture maximale de l'environnement.

---

## Technologies utilisées

| Technologie | Utilisation |
|------------|-------------|
| Python | Développement du programme |
| dronecmds | Contrôle du drone virtuel |
| Drone Virtual Simulator | Simulation de l'environnement |

---

##  Complexité de l'algorithme

La complexité de l'exploration est proportionnelle au volume discret de la salle :

**Complexité temporelle :**
O(L × l × h)

où :

- L représente la longueur de la salle ;
- l représente la largeur de la salle ;
- h représente le nombre de couches de hauteur explorées.

Cette approche garantit la découverte de la cible si celle-ci se trouve dans la zone explorée.

---

## Contraintes prises en compte

- Respect d'une marge de sécurité vis-à-vis des murs.
- Prévention des collisions.
- Détection en temps réel de la cible.
- Adaptation aux dimensions de la salle.
- Gestion des exceptions d'exécution.

---

##  Résultats obtenus

Le programme permet :

✔ L'exploration autonome d'un environnement 3D.  
✔ La recherche systématique d'une cible inconnue.  
✔ La détection et l'arrêt automatique du drone.  
✔ Une couverture complète de la zone de recherche.  
✔ Une simulation réaliste des problématiques de navigation autonome.

---

## Perspectives d'amélioration

Plusieurs pistes d'évolution peuvent être envisagées :

- Optimisation du trajet par algorithmes de pathfinding.
- Intégration d'une cartographie dynamique.
- Utilisation de capteurs simulés plus avancés.
- Réduction du temps de recherche.
- Adaptation à des environnements comportant des obstacles.

---

##  Auteur

** Mohamed Lamine Bah**  
Étudiant en Business Data Science  
Université Catholique de l'Ouest (UCO)

---

## Licence

Projet académique réalisé dans le cadre d'un enseignement universitaire d'algorithmique et de programmation Python.
