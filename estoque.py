import os
from time import sleep

def menu():
	os.system('cls')
	print('='*25)
	print('')
	print('================CONTROLE DE ESTOQUE===============')
	print('='*25)
	print('')
	print('Menu Principal')
	print('1-Produtos em Estoque')
	print('2-Cadastro de Produtos')
	print('3-Excluir Produtos')
	escolhamenu = int(input())
	if escolhamenu == 1:
		estoque()
	elif escolhamenu == 2:
		cadastro()
	elif escolhamenu == 3:
		excluir()
	else:
		print('OPCAO INVALIDA! TENTE NOVAMENTE')
		sleep(3)
		menu()


def estoque():
	os.system('cls')
	print('='*25)
	print('')
	print('================CONTROLE DE ESTOQUE===============')
	print('='*25)
	print('')
	print('Produtos em Estoque')
	for c in range(0, len(estoquelist)):
		print('{}-{}'.format(c+1, estoquelist[c]))
	print('')
	print('Digite:')
	print('1-Voltar ao Menu')
	print('2-Sair do programa')
	escolhaestoque = int(input())
	if escolhaestoque == 1:
		menu()
	elif escolhaestoque == 2:
		exit()
	else:
		print('OPCAO DIGITADA INVALIDA!')
		sleep(3)
		cadastro()		

def cadastro():
	os.system('cls')
	print('='*25)
	print('')
	print('================CONTROLE DE ESTOQUE===============')
	print('='*25)
	print('')
	print('Cadastro de Produtos')
	print('')
	r = 1
	while(r == 1):
		novoproduto = input('Produto: ')
		estoquelist.append(novoproduto)
		print('Produto cadastrado!')
		print('Cadastrar outro produto?')
		n = int(input('1-Sim 2-Menu'))
		r = n
	if r == 2:
		menu()	

def excluir():
	os.system('cls')
	print('='*25)
	print('')
	print('================CONTROLE DE ESTOQUE===============')
	print('='*25)
	print('')
	print('Produtos em Estoque')
	for c in range(0, len(estoquelist)):
		print('{}-{}'.format(c+1, estoquelist[c]))
	codigoexclusao = int(input('Digite o codigo do produto que deseja excluir:'))
	v = codigoexclusao - 1
	estoquelist.pop(v)
	print('Produto Excluido!')
	print('')
	print('1-Excluir outro produto')
	print('2-Menu Principal')
	escolhaexcluir = int(input())
	if escolhaexcluir == 1:
		excluir()
	elif escolhaexcluir == 2:
		menu()
	else:
		print('OPCAO INVALIDA!')
		sleep(3)
		menu()		








estoquelist = []	
menu()	
					