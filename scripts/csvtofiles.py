with open ('/home/pedrotorres/Documents/UFC/TCC/implementacao/GIST/gistdescriptor/csv/gist_features_w_real.csv', 'r') as f:
	i = 1
	for line in f:
		with open ('/home/pedrotorres/Documents/UFC/TCC/implementacao/GIST/gistdescriptor/txt/files/{}.txt'.format(i), 'w') as f_:
			f_.write(line)
		i = i + 1
