#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import numbers
import time
import random
from numpy.random import choice
import itertools

class Dupla(object):
	
	"""Uma dupla que participa da competição tem as seguintes propriedades:

	Attributes:
        name_1: nome do indivíduo 1
	name_2: nome do indivíduo 2
	name_1: pontos individuais do indivíduo 1
	name_2: pontos individuais do indivíduo 2
	points: numero de pontos atribuído à dupla
	lista_funcao: lista de posições sorteadas. A última vai ser desempenhada na próxima rodada. (Opções: 1,2,3,4, referente a ordem de fala)
	"""

	def __init__(self, name_1, name_2):
        	self.name1 = name_1
        	self.name2 = name_2
		self.point1 = 0
		self.point2 = 0
		self.points = 0
		self.proxima_funcao = []

	#adicionar pontos individuais
	def ind_points(self, point_1, point_2):
		try:
			self.point1 += int(point_1)
			self.point2 += int(point_2)
			return self.point1, self.point2
		except:
			raise RuntimeError( "Formato de pontos inválido, checar: " + str(point1) + str(point2))


	#adicionar pontos da dupla
	def add_points(self, n_points):
		try:
			self.points += int(n_points)
			return self.points
		except:
			raise RuntimeError( "Formato de pontos inválido, checar: " + str(n_points))
	
	#adicionar posição de fala
	def add_position(self, position):
		try:
			self.proxima_funcao.append(position)

		except:
			raise RuntimeError ('Posição de fala inválida, checar: ' + str(position))

def checa_tabela(tabela1,tabela2):

	#checa se tabelas são iguais
	if np.array_equal(tabela1,tabela2) == False:
		raise RuntimeError( "Tabelas são diferentes")


	#checa se tabela está com todos os espaços preenchidos
	for i in tabela1:
		if len(i) != len(tabela1[0]):
			raise RuntimeError( "Tabelas incompletas, olhar item " + str(i))

	#checa se o número de duplas é divisível por 4	
	n_duplas = len(tabela1)
	if n_duplas % 4 != 0 :
		raise RuntimeError( "Número de duplas não é divisível por quatro, inserir mais duplas na tabela")

#parâmetros para classificação são pontuação da dupla e média individual
def getKey(dupla):
	return dupla.points, (dupla.point1+dupla.point2)/2

#função que lê dados da tabela, cria array de objetos Duplas e devolve array ordenado por pontos
def atualiza_dados(forma_tabela):
	lista_duplas = []
	for i in forma_tabela:
		d = Dupla(i[0],i[1])
		for j in list(i)[2:]:
			#d.add_points(j[0])
			d.add_points((float(j[4:6])+float(j[7:9]))/2)
			d.add_position(j[2])
			d.ind_points(j[4:6],j[7:9])
		lista_duplas.append(d)
	return sorted(lista_duplas, key=getKey)

def chunks(l, n):
	return [l[i:i + n] for i in xrange(0, len(l), n)]

#função que imprime todas as características da classe Dupla
def imprime(uma_dupla):
	return uma_dupla.name1,uma_dupla.point1,uma_dupla.name2,uma_dupla.point2,uma_dupla.points
#,uma_dupla.points,uma_dupla.proxima_funcao


#função que sorteia funções baseadas nas funções já ocupadas pelas duplas
#recebe um chunk e retorna uma matriz com as posições
def sorteia_funcoes(chunk):
	#for dupla in chunk:
		#print imprime(dupla)

	#lista com as posições que ocuparam em ordem
	n = []
	for i in chunk:
		n.append(i.proxima_funcao)

	#posições possíveis
	p = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

	#numero de vezes que ocuparam cada posição
	#cada coluna corresponde a uma dupla, cada linha corresponde a uma função exercida
	v = np.zeros((4,4))
	for i in range(len(n)):
		v[0][i] = n[i].count('1')
		v[1][i] = n[i].count('2')
		v[2][i] = n[i].count('3')
		v[3][i] = n[i].count('4')


	#numero de rodadas que já foram é o comprimento de cada array(assumimos que o array está com as dimensões corretas)
	rodadas = len(n[0])

	#calcula matriz ideal de vezes que cada dupla deveria ter exercido cada função
	valor_ideal = np.full((4,4), rodadas/4.)

	a = itertools.permutations(p, 4)

	#lista de matrizes com todas a combinações
	todas = []
	m = []

	for i in a:
		todas.append(np.reshape(i,(4,4)))
		m.append(np.sum((np.reshape(i,(4,4)) + v - valor_ideal)**2))

	#matriz com índice medidas
	#print m


	min_value = min(m)
	indexes_with_min_value = [i for i in range(0,len(m)) if m[i] == min_value]

	#print v
	matriz_proxima = (todas[random.choice(indexes_with_min_value)])
	#print matriz_proxima 

	for i in range(len(matriz_proxima )):
		for j in range(len(matriz_proxima )):
			if matriz_proxima[j][i] == 1:
				print "Dupla "  + str(chunk[i].name1) + " e " +  str(chunk[i].name2) + " são " + str(j+1) + " a falar"



	#print v

	#print valor_ideal

	#print (v-valor_ideal)**2


#função que pega lista de duplas e separa em grupos
#se é a primeira rodada, o sorteio é aleatório
#se a rodada é classificatória, o sorteio é baseado em pontos
def sorteia_proxima(forma_tabela):

	#o número de rodadas é tomado como o número de colunas da tabelas menos 2 colunas (onde estão os nomes)
	rodada_atual = len(forma_tabela[0])-1

	#lê os dados da tabela e ordena por pontos como primeira critério e por médio da dupla como segundo critério
	lista_duplas_ordenadas = atualiza_dados(forma_tabela)

	print "Pontuação geral:"
	for dupla in lista_duplas_ordenadas:
		print imprime(dupla)#, getKey(dupla)

	print "\n"

	#na primeira rodada, os sorteios da próxima são aleatórios:
	if rodada_atual == 1:
		lista_embaralhada  = random.sample(lista_duplas_ordenadas, len(lista_duplas_ordenadas))   
		return chunks(lista_embaralhada, 4)

	else: 
		return chunks(lista_duplas_ordenadas, 4)




#mais de uma tabela para redundância
tabela1 = np.genfromtxt('planilha1.csv', names=True, delimiter=',', dtype=None)

tabela2 = np.genfromtxt('planilha2.csv', names=True, delimiter=',', dtype=None)

#print tabela1[0][1]

#checa se tabelas estão corretas
checa_tabela(tabela1, tabela2)


#sorteia proxima rodada, mostrando as duplas e as funções
for j, i in enumerate(sorteia_proxima(tabela1)):
	print "Grupo " +  str(j+1)
	sorteia_funcoes(i)
	print "\n"



		
