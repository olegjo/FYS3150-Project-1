import sys
import numpy as np
import matplotlib.pyplot as plt
import os

os.system('./Project-1-task-b-v2 1000')
f = open('Project-1-task-b-v2-output.txt')

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

plt.plot(x, v, label='Numerical')
plt.plot(x, v_anal, label = 'analytical')
plt.legend()
plt.show()