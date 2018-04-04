a = dict()
with open ('texts.clusters', 'r') as f:
	for line in f:
		line = line.split(',')
		line[1] = line[1].replace('\n', '')
		if(line[1] in a):
			a[line[1]].append(line[0])
		else:
			a[line[1]] = [line[0]]


print len(a['344'])

for i in a:
	print ('{}->{}'.format(i, len(a[i])))
