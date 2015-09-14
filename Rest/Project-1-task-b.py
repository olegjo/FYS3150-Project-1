import numpy as np
import scipy
import scipy.linalg

def f(x):
	return 100*np.exp(-10*x)

n = 2**12
n = 4
h = 1./(n+1)
x = np.linspace(0,1,n+2)

a_vec = scipy.zeros(n)
b_vec = scipy.zeros(n) + 2
c_vec = scipy.zeros(n)

a_vec[1:] -= 1
c_vec[:-1] -= 1

b_vec_tilde = h**2*f(x)

A = scipy.zeros((n,n+2))
for i in np.arange(n):
	A[i, i] = a_vec[i]
	A[i, i+1] = b_vec[i]
	A[i, i+2] = c_vec[i]

A = A[:,1:-1]

P, L, U = scipy.linalg.lu(A)

y = np.zeros(n)
y[0] = b_vec_tilde[0]/float(L[0,0])
for i in np.arange(1,n):
	s_temp = 0
	for k in np.arange(i):
		s_temp += L[i,k]*x[k]
	y[i] = (b_vec_tilde[i] - s_temp)/L[i,i]


v = np.zeros(n)
for i in np.linspace(n-1, 0, n):
	v[i] -= temp[i+1]*v[i+1]

