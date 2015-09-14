import sys
import numpy as np
import matplotlib.pyplot as plt
import os

version = 'v2'
max_err = []
ns = np.array([10, 100, 1000, 10000, 100000])
for n in ns:
	os.system('./Project-1-task-b-%s %i Project-1-task-b-%s-output_tempfile.txt' % (version, n, version))
	f = open('Project-1-task-b-%s-output_tempfile.txt' % (version))

	x = []
	v = []
	v_anal = []

	for line in f:
		numbers = line.split()
		x.append(float(numbers[0]))
		v.append(float(numbers[1]))
		v_anal.append(float(numbers[2]))

	x = np.array(x)
	v = np.array(v)
	v_anal = np.array(v_anal)
	abserr = np.log10(np.abs((v[1:-1] - v_anal[1:-1])/v_anal[1:-1])) # the first element is always 0
	max_err.append(max(abserr))
	print "n = %i    eps = log10(abs(relerr)) = %f\n" % (n, max(abserr))
	plt.figure()
	plt.plot(x, v, label='Numerical')
	plt.plot(x, v_anal, label = 'Analytical')
	#plt.title('$n=%i$' % n)
	plt.xlabel('$x$')
	plt.ylabel('$f(x)$')
	plt.legend()
	plt.savefig('FYS3150_project_1_figure_n_'+str(n)+'.pdf')

# plt.figure()
# plt.plot(ns, np.array(max_err))
# plt.show()