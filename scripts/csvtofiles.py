with open ('gist_features.csv', 'r') as f:
	i = 1
	for line in f:
		with open ('saida/{}.txt'.format(i), 'w') as f_:
			f_.write(line)
		i = i + 1
