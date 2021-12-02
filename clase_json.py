import json
from pathlib import Path

class fileJson():
	def __init__(self,pathJson):
		#self.rutaJson =
		self.rutaJson = pathJson

	def modLectura(self):
		self.file = open(self.rutaJson,"r")

	def modEscritura(self):
		self.file = open(self.rutaJson,"w")

	def get(self):
		self.file = open(self.rutaJson,"r")
		data = self.file.read()
		dataJson = json.loads(data)
		return dataJson["products"]
		self.file.close()

	def post(self,new_product):
		self.file = open(self.rutaJson,"r")
		data = self.file.read()
		print("llegue")
		print(data)
		dataJson = json.loads(data)
		lista_productos_actual = dataJson["products"]["1"]
		lista_productos_actual.append(new_product)
		dataJson = json.dumps({"products":{"1":lista_productos_actual}})
		self.file = open(self.rutaJson,"w")
		self.file.write(dataJson)
		self.file.close()

