import re

def exp_reg(s):
	s = s.replace(')', ',)')
	s = re.sub(':.*?,', ',', s)
	s = s.replace(',)', ')')
	s = re.sub(':.*?;', '', s)
	return s

tree = dict()
k = 0
k_ = 0
with open ('texts.newick', 'r') as f:
	for line in f:
		s = line
		s = exp_reg(s)
		out_ = ''
		level = 1
		aux = ''
		for i in s:
			if(i == '('):
				level = level + 1
				k_ = k_ + 1
			elif(i == ')'):
				k = k + 1
				level = level - 1

				aux = aux.replace('\'', '')
				aux = aux.split(',')
				aux = filter(len, aux)

				if level in tree:
					tree[level].append(aux)
				else:
					tree[level] = [aux]	
				aux = ''
			else:
				aux = aux + i
for i in tree:
	print (i, tree[i])

print k_
print k	