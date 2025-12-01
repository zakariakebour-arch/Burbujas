from flask import Flask,render_template
import json
import random

class Persona:
    def __init__(self,nombre,x,y,moverX,moverY):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.moverX = moverX
        self.moverY = moverY
    
    def posiciones(self):
        return {
            "nombre": self.nombre,
            "x": self.x,
            "y": self.y,
            "moverX": self.moverX,
            "moverY": self.moverY
        }


personas = ["Ana","Luis","Carla","Miguel","Sofía","Javier","María","Pedro","Lucía","Andrés","Elena","Gabriel","Valeria","Daniel","Camila","Roberto","Paula","Fernando","Diana","Santiago","Patricia","Héctor","Natalia","Rodrigo","Isabel","Tomás","Verónica","Marco","Claudia","Diego"]


lista_personas = []#Creamos una lista que contiene cada objeto creado
#Para cada persona creamos posiciones x, y y un movimiento en los dos ejes aleatorios
for persona in range(0,30):
    posiciony_aleatoria = random.randint(0,1920) #Se posiciona aleatoriamente en la pagina segun la altura
    posicionx_aleatoria = random.randint(0,1080)#Se posiciona aleatoriamente en la pagina segun la anchura
    movimientoX_aleatorio = random.randint(0,500)#Se mueve aleatorioamente despues de posicionarse hasta 500px
    movimientoY_aleatorio = random.randint(0,500)#Se mueve aleatoriamente despues de posicionarse hasta 500px como ejemplo
    indice = persona
    burbuja = Persona(personas[indice],posicionx_aleatoria,posiciony_aleatoria,movimientoX_aleatorio,movimientoY_aleatorio)
    lista_personas.append(burbuja)

personas_json = [p.posiciones() for p in lista_personas]

#Creamos la aplicacion web
app = Flask(__name__)

#Creamos la ruta principal donde se veran las personas
@app.route("/")
def principal():
    return render_template("index.html")

#Y creamos una ruta que se mandara en ella json 
@app.route("/api")
def rutaJson():
    return json.dumps(personas_json,indent=4)

if __name__ == '__main__':
    app.run(debug=True)

        