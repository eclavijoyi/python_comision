from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        comision = float(request.form['comision'])
        comision_principal = comi(comision)
        comision_extra_condicional = comision_extra(comision)

        resultado = {
            'comision_principal': comision_principal,
            'comision_extra_condicional': comision_extra_condicional,
            'comision_total': comision_principal + comision_extra_condicional
        }

    return render_template('index.html', resultado=resultado)

def comi(num):
    if num < 30400:
        return 0
    elif 30400 <= num <= 36465:
        return 90
    elif 36465 < num <= 48620:
        return 180
    elif 48620 < num <= 66852:
        return 270
    elif 66852 < num <= 91162:
        return 360
    else:
        return 450

def comision_extra(comision):
    if comision <= 91162:
        return 0
    else:
        diferenciaVenta = comision - 91162
        igv = diferenciaVenta * 0.18
        renta = diferenciaVenta * 0.03
        sumaIgvRenta = diferenciaVenta - (igv + renta)
        resultado = sumaIgvRenta * 0.008
        resultadoRedondeado = round(resultado * 100) / 100
        return resultadoRedondeado

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




