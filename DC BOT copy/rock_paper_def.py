import random

def tas_kagıt_makas_oyunu():
    print("\t""-_-ŞANS OYUNU TAŞ KAĞIT MAKAS-_-")
    print("AŞAĞIDA AÇILAN EKRANDAN SEÇİMİNİ YAP VE""\n""OYUNU KAZANMAYA ÇALIŞ. UNUTMA TAMAMEN ŞANS OYUNU :)")
    
    elements = ["🪨", "📄", "✂"]
    enemyNumber = random.randint(0, 2)
    
    
    playerNumber = int(input("Giriş yapılması bekleniyor...:"))
    
    if ((enemyNumber == 0) and (playerNumber == 0)):
        print("DRAW🤝🏽")
    elif ((enemyNumber == 0) and (playerNumber == 1)):
        print("YOU WON🏆")
    elif ((enemyNumber == 0) and (playerNumber == 2)):
        print("COMPUTER WINS💻🏆")
    elif ((enemyNumber == 1) and (playerNumber == 0)):
        print("COMPUTER WINS💻🏆")
    elif ((enemyNumber == 1) and (playerNumber == 1)):
        print("DRAW🤝🏽")
    elif ((enemyNumber == 1) and (playerNumber == 2)):
        print("YOU WON🏆")
    elif ((enemyNumber == 2) and (playerNumber == 0)):
        print("YOU WON🏆")
    elif ((enemyNumber == 2) and (playerNumber == 1)):
        print("COMPUTER WINS💻🏆")
    else:
        print("DRAW🤝🏽")

# Fonksiyonu çağırarak oyunu başlatabilirsiniz
#tas_kagıt_makas_oyunu()
