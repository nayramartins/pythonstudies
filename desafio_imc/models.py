class Pessoa(object):
	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def imprimir(self):
		peso_int = float(self.peso)
		altura_int = float(self.altura)
		calc_imc = peso_int / (altura_int * altura_int)

		print("%s o seu IMC é %s") % (self.nome, calc_imc)