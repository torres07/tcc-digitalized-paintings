import os
import sys

def main(argv):
	for i in argv:
		file_ = int(i)
		if (file_ >= 1 and file_ <= 389):
			os.system('gnome-open ../movimentos-artisticos/cubismo_{}.jpg'.format(file_))
		elif (file_ >= 390 and file_ <= 751):
			os.system('gnome-open ../movimentos-artisticos/expressionismo_{}.jpg'.format(file_ - 389))
		elif (file_ >= 752 and file_ <= 1114):
			os.system('gnome-open ../movimentos-artisticos/romantis_{}.jpg'.format(file_ - 751))
		else:
			print 'file doesnt exist'

if __name__ == "__main__":
   main(sys.argv[1:])