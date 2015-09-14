import numpy as np
import matplotlib.pyplot as plt

x = []
v = []
v_anal = []

f = open('armadillo_results.txt')
for line in f:
	numbers = line.split()
	x.append(float(numbers[0]))
	v.append(float(numbers[1]))
	v_anal.append(float(numbers[2]))

x = np.array(x)
v = np.array(v)
v_anal = np.array(v_anal)
abserr = np.log10(np.abs((v[1:-1] - v_anal[1:-1])/v_anal[1:-1])) # the first element is always 0
print max(abserr)

plt.plot(x, v, label='Numerical')
plt.plot(x, v_anal, label='Analytical')
plt.legend()
#plt.show()
