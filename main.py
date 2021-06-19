from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import auswertungen
from json import loads

import daten

app = Flask("Healthoo")

#Wir teilen der App mit, welche URL was ausführen soll. Wir definieren die Funktion die beim Aufruf der URL ausgeführt werden soll und was diese Funktion zurückgeben soll.
#Man setzt für Variable Name aus Template einen Wert ein
@app.route('/')
def startseite():
    return render_template("vorlage.html")


@app.route('/erfassen',methods=['GET', 'POST'])
def erfassen():
    if request.method == 'POST':
        menge = request.form['menge']
        lebensmittel=request.form["lebensmittel"]
        rueckgabe_string = "Du hast " + menge + " von "+lebensmittel+" zu dir genommen. Deine Daten wurden erfasst."
        liste=[lebensmittel,menge]
        zeitpunkt, aktivitaet = daten.aktivitaet_speichern(liste)
        return rueckgabe_string
    return render_template('erfassen.html')


with open('aktivitaeten.json') as open_file:
    json_als_string = open_file.read()
    mein_eingelesenes_dict = loads(json_als_string)
woche = reversed(auswertungen.wochentag_definieren())
kcal = reversed(auswertungen.auswerten_letzteWoche(mein_eingelesenes_dict))

def data():

    df = pd.DataFrame(list(zip(woche,kcal)), columns = ['Wochentag','Kcal'])
    return df
magnesium = auswertungen.auswerten_magnesium_woche(mein_eingelesenes_dict)
rest = 2100 - magnesium
liste = []
liste.append(magnesium)
liste.append(rest)
def data2():
    df2 = pd.DataFrame(liste, columns=["Wert"])
    return df2

def viz():
    df = data()

    fig = px.bar(
        df,
        x='Wochentag', y='Kcal',
        labels={
            'Wochentag': 'Wochentag',
            'Kcal': 'Kcal'
        },
        height=400
    )

    div = plot(fig, output_type="div")
    return div

def viz2():
    df2 = data2()
    name = ['Magnesium', "Fehlt bis zur Deckung"]
    fig = px.pie(df2,values="Wert",names=name)

    div2 = plot(fig, output_type="div")
    return div2

@app.route('/auswertungen')
def auswertungen():
    div = viz()
    div2=viz2()
    return render_template('auswertungen.html',viz_div=div,viz_div2=div2)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

