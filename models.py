# -*- coding: UTF-8 -*-

class Perfil():
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def obter_curtidas(self):
		return self.__curtidas

	def curtir(self):
		self.__curtidas+=1

	def imprimir(self):
		print("Nome: %s, telefonelefone: %s, Empresa: %s") % (self.nome, self.telefone, self.empresa)