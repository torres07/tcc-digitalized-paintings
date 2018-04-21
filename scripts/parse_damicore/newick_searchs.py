# -*- coding: utf-8 -*-
# @Author: Pedro Torres
# @Date:   2018-04-18 13:34:55
# @Last Modified by:   Pedro Torres
# @Last Modified time: 2018-04-21 19:29:19

import random
import numpy as np
from Bio import Phylo

#LBP
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/LBP/lbp.newick', 'newick')

#GIST
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/GIST/gist.newick', 'newick')

# COLOR
tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/COLOR/color.newick', 'newick')


# order ({'preorder', 'postorder', 'level'}) - Tree traversal order: 'preorder' (default) is depth-first search, 'postorder' is DFS with child nodes preceding parents, and 'level' is breadth-first search.

def search(search_order, n):
	S = []
	
	for clade in tree.find_clades(order=search_order):
		if clade.is_terminal():
			S.append(clade.name)

	rnd = random.randint(0, len(S) - 1)
	while (len(S[rnd:rnd + n]) < n): 
		rnd = random.randint(0, len(S) - 1)

	return S[rnd:rnd + n]


def files_random(n):
	txts = []
	for i in range(n):
		file_ = random.randint(1, 1114)
		txts.append(file_)
	return txts

def concat_txt(s):
	s = s + ('.txt')
	return s

def euclidian_distances(descs, n_pinturas, outs = []):
	if(descs == 'color'):
		dir_ = '/home/pedrotorres/Documents/UFC/TCC/implementacao/COLOR/txt/files'
	if(descs == 'gist'):
		dir_ = '/home/pedrotorres/Documents/UFC/TCC/implementacao/GIST/gistdescriptor/txt/files'
	if(descs == 'lbp'):
		dir_ = '/home/pedrotorres/Documents/UFC/TCC/implementacao/LBP/txt/files'

	if(outs == []):
		txts = files_random(n_pinturas)
	else:
		outs = outs.split(' ')
		txts = outs[:len(outs) - 1]

	elems = []
	for t in txts:
		list_ = []
		with open('{}/{}.txt'.format(dir_, t), 'r') as f:
			for line in f:
				list_ = line.split(',')
				nplist = np.array(map(float, list_))			
				elems.append(nplist)

	distance_matrix = []

	for i in range(len(elems)):
		distance_matrix.append([])
		for j in range(len(elems)):
			distance_matrix[i].append(0)
	
	for i in range(len(elems)):
		for j in range(len(elems)):
			distance_matrix[i][j] = np.linalg.norm(elems[i] - elems[j])

	avg_ = 0.0
	c_ = 0.0
	for i in range(len(elems)):
		for j in range(len(elems)):
			if i != j:
				c_ = c_ + 1.0
				avg_ = avg_ + distance_matrix[i][j]
	
	avg_ = avg_ / c_

	return avg_


def branch_distances(tree, n_pinturas, outs = []):
	if(outs == []):
		txts = files_random(n_pinturas)
		txts = map(str, txts)
	else:
		outs = outs.split(' ')
		txts = outs[:len(outs) - 1]

	elems = []
	elems = map(concat_txt, txts)

	branch_matrix = []

	for i in range(len(elems)):
		branch_matrix.append([])
		for j in range(len(elems)):
			branch_matrix[i].append(0)
	
	for i in range(len(elems)):
		for j in range(len(elems)):
			i_ = tree.find_any(elems[i])
			j_ = tree.find_any(elems[j])
			branch_matrix[i][j] = tree.distance(i_,j_)

	avg_ = 0.0
	c_ = 0.0
	for i in range(len(elems)):
		for j in range(len(elems)):
			if i != j:
				c_ = c_ + 1.0
				avg_ = avg_ + branch_matrix[i][j]
	
	avg_ = avg_ / c_

	return avg_

def gerar_dados_exposicoes(desc, n_exp, n_pinturas, method, tree=''):

	l_0 = []
	l_1 = []
	l_2 = []
	l_3 = []

	for i in range(n_exp):
		files__ = search('level', n_pinturas)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		if method == 'euclidian':
			l_0.append(euclidian_distances(desc, n_pinturas, out_))
		if method == 'branch':
			l_0.append(branch_distances(tree, n_pinturas, out_))
	
	print('level end')

	for i in range(n_exp):
		files__ = search('preorder', n_pinturas)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		if method == 'euclidian':
			l_1.append(euclidian_distances(desc, n_pinturas, out_))
		if method == 'branch':
			l_1.append(branch_distances(tree, n_pinturas, out_))

	print('preorder end')

	for i in range(n_exp):
		files__ = search('postorder', n_pinturas)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		if method == 'euclidian':
			l_2.append(euclidian_distances(desc, n_pinturas, out_))
		if method == 'branch':
			l_2.append(branch_distances(tree, n_pinturas, out_))

	print('postorder end')

	for i in range(n_exp):
		if method == 'euclidian':
			l_3.append(euclidian_distances(desc, n_pinturas))
		if method == 'branch':
			l_3.append(branch_distances(tree, n_pinturas))

	print('random end')
	
	return l_0 + l_1 + l_2 + l_3

print 'color'
print gerar_dados_exposicoes('color', 100, 12, 'branch', tree)

# saida = ''
# pinturas = search('postorder', 12)

# for i in pinturas:
# 	saida = saida + i.split('.')[0] + ' '

# print saida