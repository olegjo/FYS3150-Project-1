import os
import sys

program = sys.argv[1]
os.system('g++ -c -Wall %s -larmadillo -lblas -llapack' % program)
program = program[:-4]
os.system('g++ -o %s %s.o -larmadillo -lblas -llapack' % (program, program))
os.system('/.%s' % program)
