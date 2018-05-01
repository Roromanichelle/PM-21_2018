gueltige_nukleotide = ['A', 'T', 'G', 'C']

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
mw_a = 313210
mw_t = 304200
mw_g = 329210
mw_c = 289180
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mw_oh = 17010


def hole_dna_sequenz():
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.
    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    A, G, T, C, a, g, t, c bestehen.
    """

    # Hinweis: Verwende eine while-Schleife, innerhalb derer Du eine
    # Sequenz vom Nutzer erfragst und die Eingabe validierst.
    # Nur wenn die Validierung klappt, brichst Du die Schleife ab
    # und lieferst die Sequenz zurück.
    a=True 
    while a :
        sequence = input('Gib eine DNA-Sequenz ein: ')        
        a=False
        for i in sequence.upper() :
            if i not in gueltige_nukleotide:
                print('Bei der Eingabe handelt es sich nicht um eine gültige '
                'DNA-Sequenz!')
                a=True
                break
    return sequence


seq = hole_dna_sequenz()
SEQ = seq.upper()
# Hier sollten jetzt die nötigen Berechnungen durchgeführt werden.

# Und hier erfolgt dann die Ausgabe.



print()

print('Eingelesene Sequenz: ', SEQ)

print()

print('länge :', len(SEQ) )

print()

print('Base','  ','Häufigkeit')
print('G','     ', SEQ.count('A'))
print('C','     ', SEQ.count('C'))
print('T','     ', SEQ.count('T'))
print('A','     ', SEQ.count('A'))

print()

print('% GC-Gehalt :',((SEQ.count('C')+SEQ.count('G'))/len(SEQ))*100)

mw_ADN = {'A' : mw_a, 'T' : mw_t, 'C' : mw_c, 'G' : mw_g}

mw = 0
for k,i in mw_ADN.items() : 
    mw = mw + SEQ.count(k)*i

mw = (mw+mw_oh)/1000

print()

print('Molekulargewicht : ',mw,'g/mol')

print()