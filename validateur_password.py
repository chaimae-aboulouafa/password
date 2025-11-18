def validateur(password):
    if len(password) < 8 or len(password) > 40:
        print("Le mot de passe doit contenir entre 8 et 40 caractères")
        return False
    minuscule= False
    majuscule= False
    chiffre= False
    special= False
    for i in range(len(password)):
        if password[i]>= "a" and password[i]<= "z":
            minuscule = True
        if password[i]>= "A" and password[i]<= "Z":
            majuscule= True
        if password[i]>= "0" and password[i]<= "9":
            chiffre = True 
        if (password[i]== "!" or password[i]=="@" or password[i]== "#" or password[i]== "$" or password[i]== "%" or password[i]=="^" or password[i]=="&"):
            special = True
    if not minuscule:
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        return False
    if not majuscule:
        print("Le mot de passe doit contenir au moins une lettre majuscule")
        return False
    if not chiffre:
        print("Le mot de passe doit contenir au moins une chiffre")
        return False
    if not special:
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &)")
        return False
    return True



while True:
    mot = input("Donnez un mot de passe : ")

    if validateur(mot):
        print("Mot de passe accepté.")
        break
    else:
        print("Mot de passe refusé, réessayez. \n")
    
     