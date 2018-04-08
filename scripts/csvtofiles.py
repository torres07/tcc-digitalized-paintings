with open ('/home/pedrotorres/Documents/UFC/TCC/implementacao/LBP/csv/lbp_features_w_real.csv', 'r') as f:
	i = 1
	for line in f:
		with open ('/home/pedrotorres/Documents/UFC/TCC/implementacao/LBP/txt/files/{}.txt'.format(i), 'w') as f_:
			f_.write(line)
		i = i + 1
