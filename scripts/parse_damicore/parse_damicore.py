with open ('texts2.clusters', 'r') as f:
	for line in f:
		line = line.replace('(', '')
		line = line.replace(':', '')
		line = line.split(')')
		list_ = []
		for i in line:
			i = i.split(',')
			list__ = []
			for j in i:
				pos = j.find('txt')
				if (pos != -1):
					j = j[0:pos + 4]
					list__.append(j)
			if(len(list__)):
				list_.append(list__)

# print list_[::-1]
print list_
