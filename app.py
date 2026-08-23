from flask import Flask, render_template
import json

app = Flask(__name__)

# Cesta 1: Úvodní stránka (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Cesta 2: Koncerty (koncerty.html)
@app.route('/koncerty')
def koncerty():
    with open('koncerty.json', 'r', encoding='utf-8') as f:
        seznam_koncertu = json.load(f)
    return render_template('koncerty.html', koncerty_do_html=seznam_koncertu)

# Cesta 3: Hudba (hudba.html)
@app.route('/hudba')
def hudba():
    with open('pisnicky.json', 'r', encoding='utf-8') as f:
        seznam_pisnicek = json.load(f)
    return render_template('pisne.html', pisnicky_do_html=seznam_pisnicek)

@app.route('/galerie')
def galerie():
    with open('galerie.json','r',encoding='utf-8') as f:
        alba=json.load(f)
    return render_template('galerie.html',alba_do_html=alba)


# Ty špičaté závorky <id_alba> říkají Flasku, že cokoliv uživatel zadá za /galerie/,
# má vzít a vložit to do proměnné id_alba
@app.route('/galerie/<id_alba>')
def detail_alba(id_alba):
    # 1. Načteme celou naši JSON databázi
    with open('galerie.json', 'r', encoding='utf-8') as f:
        vsechna_alba = json.load(f)
        
    # 2. Musíme najít to konkrétní album, na které uživatel kliknul
    hledane_album = None
    for album in vsechna_alba:
        if album['id'] == id_alba:
            hledane_album = album
            break
            
    # 3. Pokud někdo zadal do adresy nesmysl, pošleme chybovou hlášku
    if hledane_album is None:
        return "Album nenalezeno", 404
        
    # 4. Pokud jsme ho našli, pošleme jen to JEDNO album do nové šablony
    return render_template('album_detail.html', album=hledane_album)

if __name__ == '__main__':
    app.run(debug=True)