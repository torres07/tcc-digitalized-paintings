import random
import numpy as np
from Bio import Phylo

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

def files_per_level(n, e):
	files_ = []
	for i in tree_:
		for j in tree_[i]:
			files_.append(j)
	if e == 0:
		return files_[0:n]			
	else:
		return files_[(12 * e): (n * (e + 1))]

def files_per_level_reverse(n, e):
	files_ = []
	keys = list(reversed(sorted(tree_.keys())))
	for i in keys:
		for j in tree_[i]:
			files_.append(j)
	if e == 0:
		return files_[0:n]			
	else:
		return files_[(12 * e): (n * (e + 1))]
		

def count_nodes():
	c = 0
	for i in tree_:
		for j in tree_[i]:
			c = c + 1
	return c


def concat_txt(s):
	s = s + ('.txt')
	return s

def files_per_depth(n, e):
	tree__ = []
	labels = []
	for i in range(count_nodes() + 1):
	 	tree__.append([])
	 	labels.append(False)
	for i in tree_:		
		f_ = 1
		while i + f_ not in tree_:
			f_ = f_ + 1
			if f_ > tree_.keys()[len(tree_) - 1]:
				break
		if (i + f_ in tree_):
			for j in tree_[i]:
				j = j.split('.')
				j = int(j[0])
				for k in tree_[i + f_]:
					k = k.split('.')
					k = int(k[0])
					tree__[j].append(k)

	S = []
	S_ = []
	S.append(int(tree_[tree_.keys()[0]][0].split('.')[0]))
	labels[int(tree_[tree_.keys()[0]][0].split('.')[0])] = True
	
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

	if e == 0:
		return S_[0:n]			
	else:
		return S_[(12 * e): (n * (e + 1))]

def files_random(n):
	txts = []
	for i in range(n):
		file_ = random.randint(1, 1114)
		txts.append(file_)
	return txts

def call(n, descs, random = False):
	if(random):
		for i in range(n):
			get_average(descs)
	else:
		for i in range(n):
			out_ = ''
			files__ = files_per_level_reverse(12, i)
			for i in files__:
				i = i.split('.')[0]
				out_ = out_ + i + ' '
			get_average(descs, out_)



def euclidian_distances(descs, outs = []):
	if(descs == 'color'):
		dir_ = '/home/pedrotorres/Documents/UFC/TCC/implementacao/COLOR/txt/files'
	if(descs == 'gist'):
		dir_ = '/home/pedrotorres/Documents/UFC/TCC/implementacao/GIST/gistdescriptor/txt/files'
	if(descs == 'lbp'):
		dir_ = '/home/pedrotorres/Documents/UFC/TCC/implementacao/LBP/txt/files'

	if(outs == []):
		txts = files_random(12)
	else:
		outs = outs.split(' ')
		txts = outs[:len(outs) - 1]

	elems = []
	for t in txts:
		list_ = []
		with open('{}/{}.txt'.format(dir_, t)) as f:
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
			distance_matrix[i][j] = np.round(np.linalg.norm(elems[i] - elems[j]), decimals = 2)

	avg_ = 0.0
	c_ = 0.0
	for i in range(len(elems)):
		for j in range(len(elems)):
			if i != j:
				c_ = c_ + 1.0
				avg_ = avg_ + distance_matrix[i][j]
	
	avg_ = avg_ / c_

	return avg_

def gerar_dados_exposicoes(desc, n_exp, n_pinturas):

	l_0 = []
	l_1 = []
	l_2 = []
	l_3 = []

	for i in range(n_exp):
		files__ = files_per_level(n_pinturas, i)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		l_0.append(euclidian_distances(desc, out_))

	for i in range(n_exp):
		files__ = files_per_level_reverse(n_pinturas, i)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		l_1.append(euclidian_distances(desc, out_))

	for i in range(n_exp):
		files__ = files_per_depth(n_pinturas, i)
		out_ = ''
		for i in files__:
			i = i.split('.')[0]
			out_ = out_ + i + ' '
		l_2.append(euclidian_distances(desc, out_))

	for i in range(n_exp):
		l_3.append(euclidian_distances(desc))

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

# print gerar_dados_exposicoes('lbp', 10, 102)

# print ('GIST')
# tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/GIST/gist.newick', 'newick')
# build_tree(tree)

# print gerar_dados_exposicoes('gist', 10, 102)

print ('COLOR')
tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/COLOR/color.newick', 'newick')
build_tree(tree)

print gerar_dados_exposicoes('color', 10, 102)
