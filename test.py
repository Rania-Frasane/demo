# Fonction pour demander le nom de l'utilisateur
def demander_nom():
    nom = input('Quel est votre nom ? ')
    while not nom:  # Vérifie si l'utilisateur n'a pas laissé l'entrée vide
        print("Vous devez entrer un nom.")
        nom = input('Quel est votre nom ? ')
    return nom

# Fonction principale du programme
def programme_principal():
    # Afficher un message d'accueil
    print('hello world')

    # Demander le nom à l'utilisateur
    nom = demander_nom()

    # Afficher un message personnalisé
    print(f'Bonjour {nom}, content de vous rencontrer!')

    # Poser une autre question
    age = input('Quel est votre âge ? ')
    while not age.isdigit():  # Vérifie si l'âge est un nombre
        print("L'âge doit être un nombre.")
        age = input('Quel est votre âge ? ')
    
    # Afficher un message avec l'âge
    print(f'Vous avez {age} ans. Génial !')

# Lancer le programme
programme_principal()
