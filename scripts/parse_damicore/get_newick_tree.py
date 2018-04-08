from Bio import Phylo

tree_ = dict()

#tree = Phylo.read('/home/pedrotorres/Documents/UFC/TCC/implementacao/damicore/COLOR/color.newick', 'newick')

tree = Phylo.read('/home/pedrotorres/tmp/louco.newick', 'newick')

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
	for i in tree_:
		for j in tree_[i]:
			if(len(files_) < n):
				files_.append(j)
	return files_

def files_per_level_reverse(n):
	files_ = []
	keys = list(reversed(sorted(tree_.keys())))
	for i in keys:
		for j in tree_[i]:
			if(len(files_) < n):
				files_.append(j)
	return files_			

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
	for i in tree_:
		if (i + 1 in tree_):
			for j in tree_[i]:
				j = j.split('.')
				j = int(j[0])
				for k in tree_[i + 1]:
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
			k = k + 1

	S_ = map(str, S_)
	S_ = map(concat_txt, S_)

	if n <= len(S_):
		return S_[0:n]

# files__ = files_per_level(10)
# files__ = files_per_level_reverse(10)
files__ = files_per_depth(20)

out_ = ''
for i in files__:
	i = i.split('.')[0]
	out_ = out_ + i + ' '

print out_
