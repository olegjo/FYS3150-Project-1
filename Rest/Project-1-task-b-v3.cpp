#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>
#include "time.h"

using namespace std;

double f(double x);
double anal_solution(double x);

int main(int argc, char* argv[])
{
	clock_t start, finish;
	start = clock();

	int n = atoi(argv[1]);
	double h = 1.0/(n + 1);
	double* x = new double[n];
	double* a = new double[n];
	double* b = new double[n];
	double* c = new double[n];
	double* b_tilde = new double[n];
	double* v = new double[n+1];
	double* v_anal = new double[n];

	// Assign values to a, b and c
	int i;
	for(i = 0; i < n; i++){
		a[i] = -1;
		b[i] = 2;
		c[i] = -1;
	}
	a[0] = 0;
	c[n-1] = 0;
	// Assign values to the vectors x and b_tilde
	x[0] = 0;
	b_tilde[0] = h*h*f(x[0]);
	for (i = 1; i < n; i++){
		x[i] = i*h;
		b_tilde[i] = h*h*f(x[i]);
	}









	// do the forward substitution: making all elements in a = 0, 
	// and adjusting the elements in b, c and b_tilde accordingly.
	// The old arrays (b, c, b_tilde) are overwritten.
	

    n--; // since we start from x0 (not x1)
    c[0] /= b[0];
    b_tilde[0] /= b[0];

    for (int i = 1; i < n; i++) {
	c[i] /= b[i] - a[i]*c[i-1];
        b_tilde[i] = (b_tilde[i] - a[i]*b_tilde[i-1]) / (b[i] - a[i]*c[i-1]);
    }

    b_tilde[n] = (b_tilde[n] - a[n]*b_tilde[n-1]) / (b[n] - a[n]*c[n-1]);

    for (int i = n; i-- > 0;) {
        b_tilde[i] -= c[i]*b_tilde[i+1];
    }

    n++;








	finish = clock();
	cout << "Compution time: " << ((finish - start*1.0)/CLOCKS_PER_SEC) << endl;
	// compute the analytical solution
	for (i = 0; i < n; i++){
		v_anal[i] = anal_solution(x[i]);
	}

	// write the data to file
	ofstream targetfile;
	targetfile.open(argv[2]);
	for (i = 0; i < n; i++){
		targetfile << setw(15) << setprecision(8) << x[i];
		targetfile << setw(15) << setprecision(8) << v[i];
		targetfile << setw(15) << setprecision(8) << v_anal[i] << endl;
	}
	targetfile.close();

	delete[] a;
	delete[] b;
	delete[] c;
	delete[] b_tilde;
	delete[] v;
	delete[] v_anal;
	return 0;
}

double f(double x){
	return 100*exp(-10*x);
} // End: function f

double anal_solution(double x){
	return 1 - (1 - exp(-10))*x - exp(-10*x);
} // End: function anal_solution















