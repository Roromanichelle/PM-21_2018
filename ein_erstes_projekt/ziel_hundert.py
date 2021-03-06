# -*- coding: utf-8 -*-

# ein einfaches Nim-ähnliches Spiel

import random    # wird in der Funktion zahl_waehlen benötigt


# ++++++++++++++++++++++++++++++++++++

# Funktionsdefinitionen:
# Aufruf erfolgt aus dem Hauptprogramm
#

def zahl_vom_spieler_holen():
    """Liefert eine vom Spieler abgefragte gültige Zahl zurück.
    
    Das ganze hier ist ein docstring.
    """
    i = True
    # solange nachfragen bis eine gültige Zahl eingegeben wird
    while i:
        zahl_als_text = input("Wieviel möchten Sie addieren?")
        try:
            zahl = int(zahl_als_text)
        except ValueError:
            print("not a number, Bitte eine Zahl von 1-10 eingeben")
        else:
            if zahl < 1 or zahl > 10:
                print("Bitte eine Zahl von 1-10 eingeben")
            else:
                i=False
    return zahl


def zahl_waehlen( e = 10 ) :
    """Liefert die nächste Zahl, die der Computer addiert."""
    
    # TO DO: die KI nochmal überdenken!
    return random.randint(1, e)


# ++++++++++++++++++++++++++++++++++++
#
# Hier beginnt das Hauptprogramm
#

print(" ZIEL HUNDERT")
print()
print("Bei jedem Zug ist eine Zahl zwischen 1 und 10 zur bisherigen")
print("Gesamtzahl zu addieren.")
print("Wer zuerst 100 erreicht, gewinnt.")
print()

# Startzahl s und Ziel e festlegen
s = zahl_waehlen( 30 )
e = 100
i=True

# Spiele los!
print("Startzahl:", s)
print()

# Wenn s den Wert von e erreicht, wird abgebrochen und der Gewinner ausgegeben
while i:
    # Zug des menschlichen Spielers
    # Zahl z von der Eingabe einlesen
    z = zahl_vom_spieler_holen()
    # z zur momentanen Summe s addieren
    s = s + z 
    print()
    print("Neuer Stand:", s)
    print()
    # Gewinnbedingung prüfen und ggf. abbrechen
    if s >= e:
        print("Sie haben gewonnen :(")
        i=False
    
    # Computerzug
    # Zahl z wählen
    z = zahl_waehlen()
    print("Ich addiere", z)
    s = s + z
    print("Neuer Stand", s)
    if s >= e:
        print("Ha, ich habe gewonnen!")
        i=False


