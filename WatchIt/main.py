def user_loop():
    print("Bienvenue dans WatchIt?")
    do_we_stop = False
    while not do_we_stop:
        user_input = input("Saissisez un nom de film : ")
        print("Vous avez tapé : {}".format(user_input))
        user_input = input("Si vous voulez continuer, tapez 'oui' : ")
        if user_input != "oui":
            do_we_stop = True
    print("Sortie de l'application WatchIt?")
            
user_loop()