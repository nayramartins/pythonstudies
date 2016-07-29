# -*- coding: UTF-8 -*-

class Perfil():
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa

	def imprimir(self):
		print("Nome: %s, Telefone: %s, Empresa: %s") % (self.nome, self.telefone, self.empresa)

class Data(object):
	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprimir(self):
		print('%s/%s/%s') % (self.dia, self.mes, self.ano)

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