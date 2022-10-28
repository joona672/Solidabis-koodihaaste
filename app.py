from flask import Flask , render_template

from DatanKasittely import *


app = Flask(__name__, template_folder='template')
sivu = ""
# with open("index.html") as index:
#     sivu = index
#     index.close()
    

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/data/<vastus1>')
def data(vastus1):
    hae(vastus1)
    hahmot = varasto.PalautaHahmot()
    hahmot = list(map(lambda x: f'<option value="{x.nimi}">', hahmot))
    hahmot = "".join(hahmot)
    varasto.Tyhjenna()
    return hahmot

@app.route('/players/<pelaaja1>/<pelaaja2>')
def haePelaajat(pelaaja1,pelaaja2):
    pelaajat = []
    hae(pelaaja1)
    hae(pelaaja2)
    pel1 = varasto.HaeValitutPelaajat(pelaaja1)
    pel2 = varasto.HaeValitutPelaajat(pelaaja2)
    pelaajat.append(pel1)
    pelaajat.append(pel2)
    return pelaajat
    
    


if __name__ == '__main__':
    app.run()
