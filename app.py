from flask import Flask, request
from clase_json import fileJson

app = Flask(__name__)

json =fileJson("data.json")

# Get Data Routes
@app.route('/products')
def getProducts():
    return json.get()


# Create Data Routes
@app.route('/products', methods=['POST'])
def addProduct():
    print("gaaaaaaaaaaaaa")
    new_product = {
        'nombre': request.json['nombre'],
        'cantidad': request.json['cantidad'],
    }
    print(new_product)
    json.post(new_product)
    return json.get()

if __name__ == '__main__':
    app.run(debug=True, port=4000)