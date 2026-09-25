from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)
numeroLed = []


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/mostrarLeds')
def showLed():
    global numeroLed
    muestra = ""
    for valor in numeroLed:
        muestra += str(valor)+","
    print(muestra)
    return str(muestra)


@app.route("/recibir", methods = ["POST"])
def getData():
    global numeroLed
    data = []
    consulta = request.form.getlist("led0")
    #data += 0 if not request.form.getlist("led0") else request.form.getlist("led0")
    for i in range(64):
        x = 0
        led = "led" + str(i)
        if not request.form.getlist(led):
            data.append(0)
        else:
            nums = request.form.getlist(led)
            for j in nums:
                x += int(j)
            data.append(x)


    numeroLed = data
    print(numeroLed)
    return redirect('/')

#######################################################################
@app.route('/bigger/<id>')
def getBigga(id):
    led = {"ancho": 0,
           "largo": 0,
           "alto" : 0}
    query = request.args.get('id')
    if query:
        led['query'] = query
    return jsonify(200, led)

@app.route('/put', methods=['POST'])
def create_led():
    data = request.get_json()
    data["status"] = "working"
    return jsonify(200, data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
