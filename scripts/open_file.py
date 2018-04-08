import os
import sys

def main(argv):
	os.system('rm ../exposicao/*')
	str_ = '['
	for i in argv:
		file_ = int(i)
		if (file_ >= 1 and file_ <= 389):
			os.system('gnome-open ../movimentos-artisticos/cubismo_{}.jpg'.format(file_))
			os.system('cp ../movimentos-artisticos/cubismo_{}.jpg ../exposicao/'.format(file_))
			str_ = str_ + '\'exposicao/cubismo_{}.jpg\','.format(file_)
		elif (file_ >= 390 and file_ <= 751):
			os.system('gnome-open ../movimentos-artisticos/expressionismo_{}.jpg'.format(file_ - 389))
			os.system('cp ../movimentos-artisticos/expressionismo_{}.jpg ../exposicao/'.format(file_ - 389))
			str_ = str_ + '\'exposicao/expressionismo_{}.jpg\','.format(file_ - 389)
		elif (file_ >= 752 and file_ <= 1114):
			os.system('gnome-open ../movimentos-artisticos/romantis_{}.jpg'.format(file_ - 751))
			os.system('cp ../movimentos-artisticos/romantis_{}.jpg ../exposicao/'.format(file_ - 751))
			str_ = str_ + '\'exposicao/romantis_{}.jpg\','.format(file_ - 751)
		else:
			print 'file doesnt exist'

	str_ = str_ + ']'
	print '################################################'
	print str_
if __name__ == "__main__":
   main(sys.argv[1:])