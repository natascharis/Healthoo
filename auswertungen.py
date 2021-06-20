import datetime
import pandas as pd
from json import loads

#Schweizer Nährwertdatenbank wird eingelesen
df = pd.read_excel('Schweizer_Nahrwertdatenbank.xlsx', engine='openpyxl')

# In Keys werden die Schlüssel abgespeichert
keys= []
#Listen für Einträge erstellen
energie=[]
fett=[]
cholesterin=[]
zucker=[]
staerke=[]
protein=[]
salz=[]
retinol=[]
betacarotin=[]
vitaminb1=[]
vitaminb2=[]
vitaminb6=[]
vitaminb12=[]
niacin=[]
vitaminc=[]
vitamind=[]
kalium=[]
natrium=[]
magnesium=[]

for row in df.itertuples(index=False):
    #Liste wird durch Namen ergänzt die sich in erster Spalte befinden
    keys.append(row[0])
    #Die Spalte für die Energie wird in Liste hinzugefügt, analog bei weiteren Vitaminen
    energie.append(row[8])
    fett.append(row[11])
    cholesterin.append(row[23])
    zucker.append(row[29])
    staerke.append(row[32])
    protein.append(row[38])
    salz.append(row[41])
    retinol.append(row[56])
    betacarotin.append(row[62])
    vitaminb1.append(row[65])
    vitaminb2.append(row[68])
    vitaminb6.append(row[71])
    vitaminb12.append(row[74])
    niacin.append(row[77])
    vitaminc.append(row[86])
    vitamind.append(row[89])
    kalium.append(row[95])
    natrium.append(row[98])
    magnesium.append(row[107])


#Es werden Dictonaries erstellt welche die Werte für alle Namen enthalten

energiedict={}
fettdict={}
cholesterindict={}
zuckerdict={}
staerkedict={}
proteindict={}
salzdict={}
retinoldict={}
betacarotindict={}
vitaminb1dict={}
vitaminb2dict={}
vitaminb6dict={}
vitaminb12dict={}
niacindict={}
vitamincdict={}
vitaminddict={}
kaliumdict={}
natriumdict={}
magnesiumdict={}

energiedict = {keys[i]: energie[i] for i in range(len(keys))}
fettdict = {keys[i]: fett[i] for i in range(len(keys))}
cholesterindict = {keys[i]: cholesterin[i] for i in range(len(keys))}
zuckerdict = {keys[i]: zucker[i] for i in range(len(keys))}
staerkedict = {keys[i]: staerke[i] for i in range(len(keys))}
proteindict = {keys[i]: protein[i] for i in range(len(keys))}
salzdict = {keys[i]: salz[i] for i in range(len(keys))}
retinoldict = {keys[i]: retinol[i] for i in range(len(keys))}
betacarotindict = {keys[i]: betacarotin[i] for i in range(len(keys))}
vitaminb1dict = {keys[i]: vitaminb1[i] for i in range(len(keys))}
vitaminb2dict = {keys[i]: vitaminb2[i] for i in range(len(keys))}
vitaminb6dict = {keys[i]: energie[i] for i in range(len(keys))}
vitaminb12dict = {keys[i]: vitaminb12[i] for i in range(len(keys))}
niacindict = {keys[i]: niacin[i] for i in range(len(keys))}
vitamincdict = {keys[i]: vitaminc[i] for i in range(len(keys))}
vitaminddict = {keys[i]: vitamind[i] for i in range(len(keys))}
kaliumdict = {keys[i]: kalium[i] for i in range(len(keys))}
natriumdict = {keys[i]: natrium[i] for i in range(len(keys))}
magnesiumdict = {keys[i]: magnesium[i] for i in range(len(keys))}




#In dieser Funktion werden die kcal für die letzte Woche berechnet
def auswerten_letzteWoche (json):
    aktuellesDatum = datetime.datetime.now()
    woche = aktuellesDatum - datetime.timedelta(days=7)
    kcal = 0
    kcal_heute=0
    kcal_gestern=0
    kcal_vorgestern=0
    kcal_vorvorgestern=0
    kcal_vorvorvorgestern=0
    kcal_vorvorvorvorgestern=0
    kcal_vorvorvorvorvorgestern=0
    #Es wird auf den kcal Wert aus dem Energiedict zugegriffen und multipliziert mit der konsumierten Menge
    for key, value in json.items():
        #Es werden nur Werte die in der letzten Woche hinzugefügt wurden berücksichtigt
        if key > str(woche):
            kcal+=((int(energiedict[str(value[0])]))/100* int(value[1]))
            datetime.datetime.strptime(key,'%Y-%m-%d %H:%M:%S.%f')
            date2=datetime.datetime.strptime(key,'%Y-%m-%d %H:%M:%S.%f')
            diff=aktuellesDatum-date2
            # Sekunden werden in Tage umgewandelt
            diff=int(diff.total_seconds()/ 60 / 60 / 24)
            #berechnen wie viele kcal innerhalb eines Tages zu sich genommen
            if diff <=1:
                kcal_heute+= ((int(energiedict[str(value[0])]))/100* int(value[1]))
            elif diff <=2:
                kcal_gestern += ((int(energiedict[str(value[0])])) / 100 * int(value[1]))
            elif diff <=3:
                kcal_vorgestern += ((int(energiedict[str(value[0])])) / 100 * int(value[1]))
            elif diff <=4:
                kcal_vorvorgestern += ((int(energiedict[str(value[0])])) / 100 * int(value[1]))
            elif diff <=5:
                kcal_vorvorvorgestern += ((int(energiedict[str(value[0])])) / 100 * int(value[1]))
            elif diff <=6:
                kcal_vorvorvorvorgestern += ((int(energiedict[str(value[0])])) / 100 * int(value[1]))
            elif diff <=7:
                kcal_vorvorvorvorvorgestern += ((int(energiedict[str(value[0])])) / 100 * int(value[1]))

            kcal_woche=[]
            kcal_woche.append(kcal_heute)
            kcal_woche.append(kcal_gestern)
            kcal_woche.append(kcal_vorgestern)
            kcal_woche.append(kcal_vorvorgestern)
            kcal_woche.append(kcal_vorvorvorgestern)
            kcal_woche.append(kcal_vorvorvorvorgestern)
            kcal_woche.append(kcal_vorvorvorvorvorgestern)
    return reversed(kcal_woche)

def auswerten_magnesium_woche(json):
    aktuellesDatum = datetime.datetime.now()
    woche = aktuellesDatum - datetime.timedelta(days=7)
    magnesium=0
    bedarf=2100

    for key, value in json.items():
        #Es werden nur Werte die in der letzten Woche hinzugefügt wurden berücksichtigt
        if key > str(woche):
            magnesium+=((int(magnesiumdict[str(value[0])]))/100* int(value[1]))
    #Für das Tortendiagramm wird für die Deckung die Differenz zwischen Wochenbedarf und aufgenommenem Magnesium benötigt
    liste=[magnesium,bedarf-magnesium]
    return liste

def auswerten_retinol(json):
    aktuellesDatum = datetime.datetime.now()
    woche = aktuellesDatum - datetime.timedelta(days=7)
    retinol=0
    bedarf=7000

    for key, value in json.items():
        #Es werden nur Werte die in der letzten Woche hinzugefügt wurden berücksichtigt
        if key > str(woche):
            retinol+=((int(retinoldict[str(value[0])]))/100* int(value[1]))
    #Es wird der Prozentsatz der Deckung berechnet
    deckung = (retinol / bedarf) * 100
    return deckung

def auswerten_vitc(json):
    aktuellesDatum = datetime.datetime.now()
    woche = aktuellesDatum - datetime.timedelta(days=7)
    vitc=0
    bedarf=665

    for key, value in json.items():
        #Es werden nur Werte die in der letzten Woche hinzugefügt wurden berücksichtigt
        if key > str(woche):
            vitc +=((int(vitamincdict[str(value[0])]))/100* int(value[1]))
    deckung = (vitc / bedarf) * 100
    return deckung

def auswerten_vitb1(json):
    aktuellesDatum = datetime.datetime.now()
    woche = aktuellesDatum - datetime.timedelta(days=7)
    vitb1=0
    bedarf=7

    for key, value in json.items():
        #Es werden nur Werte die in der letzten Woche hinzugefügt wurden berücksichtigt
        if key > str(woche):
            vitb1 +=((int(vitaminb1dict[str(value[0])]))/100* int(value[1]))
    deckung = (vitb1 / bedarf) * 100
    return deckung

def auswerten_kalium(json):
    aktuellesDatum = datetime.datetime.now()
    woche = aktuellesDatum - datetime.timedelta(days=7)
    kalium=0
    bedarf=28000

    for key, value in json.items():
        #Es werden nur Werte die in der letzten Woche hinzugefügt wurden berücksichtigt
        if key > str(woche):
            kalium +=((int(kaliumdict[str(value[0])]))/100* int(value[1]))
    deckung = (kalium / bedarf) * 100
    return deckung

def wochentag_definieren():
    aktuellesDatum = datetime.datetime.now()
    tag = datetime.datetime.today().weekday()
    tag2=6
    #Es soll eine Liste von Tagen gefüllt werden angefangen mit dem Aktuellen tag
    reihenfolge=[]
    while tag >=0:
        reihenfolge.append(tag)
        tag =tag-1
    while (len(reihenfolge))<=6:
        reihenfolge.append(tag2)
        tag2 = tag2 -1

    weekdays={0:"Montag",1:"Dienstag",2:"Mittwoch",3:"Donnerstag",4:"Freitag",5:"Samstag",6:"Sonntag"}
    wochentag = []
    for wert in reihenfolge:
        wochentag.append(weekdays[wert])

    return reversed(wochentag)





