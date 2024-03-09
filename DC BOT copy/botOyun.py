import random

def tas_kagıt_makas_oyunu(choice):
    
    elements = ["🪨", "📄", "✂"]
    enemyNumber = random.randint(0, 2)

    
    if ((enemyNumber == 0) and (choice == "TAS")):
        return "DRAW :handshake::shaking_hands:"
    elif ((enemyNumber == 0) and (choice == "KAGIT")):
        return "WIN :trophy:"
    elif ((enemyNumber == 0) and (choice == "MAKAS")):
        return "LOSE :cry:"
    elif ((enemyNumber == 1) and (choice == "TAS")):
        return "LOSE :cry:"
    elif ((enemyNumber == 1) and (choice == "KAGIT")):
        return "DRAW :handshake::shaking_hands:"
    elif ((enemyNumber == 1) and (choice == "MAKAS")):
        return "WIN :trophy:"
    elif ((enemyNumber == 2) and (choice == "TAS")):
       return "WIN :trophy:"
    elif ((enemyNumber == 2) and (choice == "KAGIT")):
        return "LOSE :cry:"
    elif (enemyNumber == 2) and (choice == "MAKAS"):
        return "DRAW :handshake:"
    else:
        return "ERROR :four: :zero: :four:"

# Fonksiyonu çağırarak oyunu başlatabilirsiniz
#tas_kagıt_makas_oyunu()
