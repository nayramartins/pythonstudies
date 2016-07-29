# -*- coding: UTF-8 -*-
def listar(nomes):
	print 'Lista de nomes:'

	for nome in nomes:
		print nome

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def alterar(nomes):
	print 'Qual nome você gostaria de alterar?'
	alterar_nome = raw_input()
	if(alterar_nome in nomes):
		posicao = nomes.index(alterar_nome)
		print 'Digite novamente'
		nome_novo = raw_input()
		nomes[posicao] = nome_novo

def procurar(nomes):
	print 'Digite o nome a procurar:'
	nome_procurar = raw_input()
	if(nome_procurar in nomes):
		print 'Nome %s encontrado' % (nome_procurar)
	else:
		print 'Nome %s não encontrado' % (nome_procurar)

def remover(nomes):
	print 'O que deseja remover:'
	item_remover = raw_input()
	nomes.remove(item_remover)

def procurar_regex(nomes):
	print('Digite a expressão regular')
	regex = raw_input()
	nomes_concatenados = "".join(nomes)

def menu():
		nomes = []
		escolha = ''
		while(escolha != '0'):
			print 'Digite 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar e 5 para pesquisar ou 0 para terminar'
			escolha = raw_input()

			if(escolha == '1'):
				cadastrar(nomes)

			if(escolha == '2'):
				listar(nomes)

			if(escolha == '3'):
				remover(nomes)

			if(escolha == '4'):
				alterar(nomes)

			if(escolha == '5'):
				procurar(nomes)
menu()				


