import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return 100*np.exp(-10*x)

def sol(x):
	return 1 - (1 - np.exp(-10))*x - np.exp(-10*x)

n = 2**12
n = 1000
h = 1./(n+1)
x = np.linspace(0,1,n+2)
a = np.zeros(n) - 1
b = np.zeros(n) + 2
c = np.zeros(n) - 1

# a[1:] -= 1
# c[:-1] -= 1

b_tilde = h**2*f(x)

## Forward Substitution:


for i in np.arange(1, n):
	b[i] = b[i-1]*b[i] - a[i]*c[i-1]
	c[i] = b[i-1]*c[i]
	b_tilde[i] = b[i-1]*b_tilde[i] - a[i]*b_tilde[i-1]
	print b_tilde[i], b[i], c[i]

## Backward Substitution
v = np.zeros(n)
v[-1] = b_tilde[-1]/b[-1]
for i in np.linspace(n-2, 0, n-1):
	v[i] = (b_tilde[i] - c[i]*v[i+1])/b[i]



plt.plot(x, sol(x), label="analytical")
plt.plot(x[2:], v, label="numerical")
plt.legend()
plt.show()






