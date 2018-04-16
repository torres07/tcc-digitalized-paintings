# -*- coding: utf-8 -*-
# @Author: Pedro Torres
# @Date:   2018-04-15 21:39:40
# @Last Modified by:   Pedro Torres
# @Last Modified time: 2018-04-16 20:58:43

import random
import numpy as np
from Bio import Phylo
from Bio.Phylo.Consensus import *

tree_ = dict()

#GIST
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/GIST/gist.newick', 'newick')

#COLOR
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/COLOR/color.newick', 'newick')

#LBP
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/LBP/lbp.newick', 'newick')

#DEBUG
#tree = Phylo.read('/home/pedrotorres/tmp/louco.newick', 'newick')

def build_tree(tree):
	for i in tree.get_terminals():
		len_ = len(tree.get_path(i))
		if(len_ in tree_):
			for j in tree.get_path(i):
				if j.name != None:
					tree_[len_].append(j.name)
		else:
			for j in tree.get_path(i):
				if j.name != None:
					tree_[len_] = [j.name]

def files_per_level(n):
	files_ = []
	start = random.randint(0, len(tree_.keys()) - 1)
	for i in tree_.keys()[start:]:
		for j in tree_[i][random.randint(0, len(tree_[i]) - 1):]:
			files_.append(j)
	
	return files_[0:n]			

def files_per_level_reverse(n):
	files_ = []
	start = random.randint(0, len(tree_.keys()) - 1)
	keys = list(reversed(sorted(tree_.keys())))
	for i in keys[start:]:
		for j in tree_[i][random.randint(0, len(tree_[i]) - 1):]:
			files_.append(j)
	return files_[0:n]			
		

def count_nodes():
	c = 0
	for i in tree_:
		for j in tree_[i]:
			c = c + 1
	return c


def concat_txt(s):
	s = s + ('.txt')
	return s

def files_per_depth(n):
	tree__ = []
	labels = []
	for i in range(count_nodes() + 1):
	 	tree__.append([])
	 	labels.append(False)
	start = random.randint(0, len(tree_.keys()) - 1)
	for i in tree_.keys()[start:]:	
		random.shuffle(tree_[i])	
		f_ = 1
		while i + f_ not in tree_:
			f_ = f_ + 1
			if f_ > tree_.keys()[len(tree_) - 1]:
				break
		if (i + f_ in tree_):
			for j in tree_[i][random.randint(0, len(tree_[i]) - 1):]:
				j = j.split('.')
				j = int(j[0])
				for k in tree_[i + f_]:
					k = k.split('.')
					k = int(k[0])
					tree__[j].append(k)

	S = []
	S_ = []
	S.append(int(tree_[tree_.keys()[start]][0].split('.')[0]))
	labels[int(tree_[tree_.keys()[start]][0].split('.')[0])] = True
	
	while(len(S)):
		u = S.pop()
		S_.append(u)
		for v in tree__[u]:
			v = int(v)
			if (not labels[v]):
				labels[v] = True
				S.append(v)
	for u in tree_[tree_.keys()[0]]:
		u = int(u.split('.')[0])
		if u not in S_:
			S_.append(u)
			labels[u] = True

	S_ = map(str, S_)
	S_ = map(concat_txt, S_)

	return S_[0:n]			

def files_random(n):
	txts = []
	for i in range(n):
		file_ = random.randint(1, 1114)
		txts.append(file_)
	return txts

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
		files__ = files_per_level(n_pinturas)
		while(len(files__) != n_pinturas):
			files__ = files_per_level(n_pinturas)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		if method == 'euclidian':
			l_0.append(euclidian_distances(desc, n_pinturas, out_))
		elif method == 'branch':
			l_0.append(branch_distances(tree, n_pinturas, out_))
	
	print('bfs end')

	for i in range(n_exp):
		files__ = files_per_level_reverse(n_pinturas)
		while(len(files__) != n_pinturas):
			files__ = files_per_level_reverse(n_pinturas)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		if method == 'euclidian':
			l_1.append(euclidian_distances(desc, n_pinturas, out_))
		elif method == 'branch':
			l_1.append(branch_distances(tree, n_pinturas, out_))

	print('bfsr end')

	for i in range(n_exp):
		files__ = files_per_depth(n_pinturas)
		while(len(files__) != n_pinturas):
			files__ = files_per_depth(n_pinturas)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		if method == 'euclidian':
			l_2.append(euclidian_distances(desc, n_pinturas, out_))
		elif method == 'branch':
			l_2.append(branch_distances(tree, n_pinturas, out_))

	print('dfs end')

	for i in range(n_exp):
		if method == 'euclidian':
			l_3.append(euclidian_distances(desc, n_pinturas))
		elif method == 'branch':
			l_3.append(branch_distances(tree, n_pinturas))


	print('random end')
	
	return l_0 + l_1 + l_2 + l_3

# files__ = files_per_level(12)
# files__ = files_per_level_reverse(12, 4)
# files__ = files_per_depth(12)
# files__ = files_random(12)

# out_ = ''
# for i in files__:
# 	i = i.split('.')[0]
# 	out_ = out_ + i + ' '

# print ('LBP DAMICORE')
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/LBP/lbp.newick', 'newick')
# build_tree(tree)

# print gerar_dados_exposicoes('lbp', 30, 32)

# print ('GIST')
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/GIST/gist.newick', 'newick')
# build_tree(tree)

# print gerar_dados_exposicoes('gist', 10, 32)

print ('COLOR')
tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/COLOR/color.newick', 'newick')
build_tree(tree)

#print gerar_dados_exposicoes('color', 10, 12, 'branch')

# print ('LOUCO DAMICORE')
# tree = (Phylo.read('/home/pedrotorres/tmp/ex.newick', 'newick'))
# build_tree(tree)

# a, b = tree.get_terminals()[:2]
# print tree.distance(a,a)


n_pinturas = 16
# files__ = files_per_level(n_pinturas)
# while(len(files__) != n_pinturas):
# 	files__ = files_per_level(n_pinturas)
# out_ = ''
# for i in files__:
# 	i = i.split('.')[0]
# 	out_ = out_ + i + ' '

# print branch_distances(tree, n_pinturas, out_)
print gerar_dados_exposicoes('color', 100, n_pinturas, 'euclidian', tree)
