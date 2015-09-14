import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return 100*np.exp(-10*x)

def sol(x):
	return 1 - (1 - np.exp(-10))*x - np.exp(-10*x)

n = 2**12
n = 10
h = 1./(n+1)
x = np.linspace(0,1,n+2)

a = np.zeros(n)
b = np.zeros(n) + 2
c = np.zeros(n)

a[1:] -= 1
c[:-1] -= 1

b_tilde = h**2*f(x)

## Forward Substitution:
b_ = np.zeros(n)
c_ = np.zeros(n)
b_tilde_ = np.zeros(n)

b_[0] = b[0]
c_[0] = c[0]
b_tilde_[0] = b_tilde[0]

for i in np.arange(1, n):
	b_[i] = b_[i-1]*b[i] - a[i]*c_[i-1]
	c_[i] = b_[i-1]*c[i]
	b_tilde_[i] = b_[i-1]*b_tilde[i] - a[i]*b_tilde_[i-1]


## Backward Substitution
v = np.zeros(n)
v[-1] = b_tilde_[-1]/b_[-1]
for i in np.linspace(n-2, 0, n-1):
	v[i] = (b_tilde_[i] - c_[i]*v[i+1])/b_[i]



plt.plot(x, sol(x), label="analytical")
plt.plot(x[2:], v, label="numerical")
plt.legend()
# plt.show()






