from flask import Flask, render_template

app = Flask(__name__) #Para confirmar que es el archivo que va a arrancar la aplicacion
@app.route('/') #creamos una ruta para la pagina principal
def home(): 
    return render_template('home.html') #para importar archivo html#

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__': 
    app.run(debug=True) #nos permite ejecutar nuestra aplicacion

