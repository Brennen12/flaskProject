from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/<choice>/<temperature>')
def convert_temperature(choice, temperature):
    if choice == "f":
        fahrenheit = float(temperature) * 9.0 / 5 + 32
        return f"The temperature {temperature} C is {fahrenheit:.2f} F"
    elif choice == "c":
        celsius = 5 / 9 * (float(temperature) - 32)
        return f"The temperature {temperature} F is {celsius:.2f} F"
    else:
        return "Invalid option"


if __name__ == '__main__':
    app.run()
