# -*- coding: utf-8 -*-
# @Author: Pedro Torres
# @Date:   2018-04-17 15:23:22
# @Last Modified by:   Pedro Torres
# @Last Modified time: 2018-04-19 06:37:42

from Bio import Phylo
import numpy as np
import random

lista_indices = []

def concat_txt(s):
	s = s + ('.txt')
	return s

def concat_idx(i, v):
	return [i, v]

def read_phylip():
	dic = []
	with open('ex.phylip', 'r') as f:
		for line in f:
			line = line.split(' ')
			lista = []
			for i in line[1:]:
				if i != '':
					i = i.replace('\n', '')
					lista.append(i)
			
			dic.append([line[0], lista])
			lista_indices.append(line[0])
	return dic


def get_nearest(n, dic):
	rnd = dic[random.randint(0, len(dic) - 1)]

	print ('escolhido: {}'.format(rnd[0]))
	
	rnd[1] = map(float, rnd[1])

	files = []
	for i in dic:
		files.append(i[0])

	rnd[1] = map(concat_idx, files, rnd[1])

	rnd[1] = sorted(rnd[1], key=lambda tup: tup[1])

	nj = []
	for i in range(n + 1):
		nj.append(rnd[1][i][0])
	return nj[:n + 1]

dic = read_phylip()
# print get_nearest(5, dic)

tree = Phylo.read('/home/pedrotorres/tmp/ex.newick', 'newick')

S = []


for clade in tree.find_clades(order='preorder'):
	if clade.is_terminal():
		S.append(clade.name)

branch_matrix = []

for i in range(len(S)):
	branch_matrix.append([])
	for j in range(len(S)):
		branch_matrix[i].append(0)

for i in range(len(S)):
	for j in range(len(S)):
		i_ = tree.find_any(S[i])
		j_ = tree.find_any(S[j])
		branch_matrix[i][j] = tree.distance(i_,j_)

k = 0
# for i in branch_matrix:
# 	print S[k]
# 	print i
# 	k = k + 1

print S
# print S[k]