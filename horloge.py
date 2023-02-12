import time
horloge_active= True
def horloge(hour, minute, second):
    if horloge_active:
        print(" ")
    while True:
        if second > 59:
            second = 0
            minute += 1
        if minute > 59:
            minute = 0
            hour += 1
        if hour > 23:
            hour = 0
            minute = 0
            second = 0
        if hour == 0 and minute == 0 and second == 5:
            print("Alarme!")
            time.sleep(1)
        print("{:02d}:{:02d}:{:02d}".format(hour, minute, second))
        second += 1
        time.sleep(1) 

heure_actuelle = (16, 30, 0)
alarme = (0, 0, 5)

def afficher_heure():
    global horloge_active
    horloge_active = False
    print(" ")
    """Affiche l'heure actuelle sous la forme hh:mm:ss"""
    heures, minutes, secondes = heure_actuelle
    print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")

def regler_heure(nouvelle_heure):
    """Règle l'heure actuelle"""
    global heure_actuelle
    heure_actuelle = nouvelle_heure

def regler_alarme(nouvelle_alarme):
    """Règle l'heure de l'alarme"""
    global alarme
    alarme = nouvelle_alarme

while True:
    afficher_heure()
    if heure_actuelle == alarme:
        print("Alarme!")
    time.sleep(1)
    heure_actuelle = time.localtime()[3:6]
    alarme = (0, 0, 0)
   
    horloge(23, 59, 58)