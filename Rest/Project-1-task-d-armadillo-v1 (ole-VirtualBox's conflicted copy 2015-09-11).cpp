#include <iostream>
#include "armadillo"
using namespace std;
using namespace arma;


/* METHOD 1:
	first create the tridiagonal matrix A (X in armadillo documentation).
	create the matrices L and U
	Perform LU decomposition by calling lu(L, U, X)
*/
int main(int argc, char *argv[])
{
	int n = 10;
	mat A;
	A.reshape(n, n);
	return 0;
}



/* METHOD 2:
	Create the tridiagonal matrix A
	Create vectors x and b where x is unknown
	call solve(x, A, b)
*/
