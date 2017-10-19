from rectangulo import rectangulo_perimetro
from flask import Flask, render_template, redirect, request

app = Flask (__name__)

@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry/')
def go_entry() -> 'html':
    return render_template('entry.html', the_title='Rectangulo',)

@app.route("/calculate/", methods=['POST'])
def calculate() -> 'html':
    a = float(request.form['a'])
    b = float(request.form['b'])
    result = rectangulo_perimetro(a,b)
    title = "Resultado del perimetro de un rectangulo"
    return render_template('results.html', the_a=a, the_b=b, the_result= result, the_title=title)

app.run(debug=True)
