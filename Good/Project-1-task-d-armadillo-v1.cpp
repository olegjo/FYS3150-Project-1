#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include "armadillo"
#include "time.h"

using namespace std;
using namespace arma;


double f(double x);
double anal_solution(double x);


int main(int argc, char* argv[])
{
	clock_t start, finish;
	start = clock();

	int n = atoi(argv[1]);
	double h = 1.0/(n + 1);
	// Creating the tridiagonal matrix A
	mat A = zeros<mat>(n,n);
	A(0,0) = 2;
	A(0,1) = -1;
	for (int i = 1; i < n-1; i++){
		A(i,i-1) = -1;
		A(i,i) = 2;
		A(i,i+1) = -1;
	}
	A(n-1, n-1) = 2;
	A(n-1, n-2) = -1;
	// cout << "A = " << endl;
	// cout << A << endl;
	mat L;
	mat U;
	lu(L, U, A);

	vec v = zeros<vec>(n);
	vec w = zeros<vec>(n);
	vec b_tilde = zeros<vec>(n);
	vec x = zeros<vec>(n);
	
	for (int i = 0; i < n; i++){
		x(i) = (i+1)*h;
		b_tilde(i) = h*h*f(x(i));
	}

	solve(w, trimatl(L), b_tilde);
	solve(v, trimatu(U), w);

	finish = clock();
	cout << "Compution time: " << ((finish - start*1.0)/CLOCKS_PER_SEC) << endl;
	
	vec v_anal = zeros<vec>(n);
	for (int i = 0; i < n; i++){
		v_anal(i) = anal_solution(x(i));
	}


	ofstream targetfile;
	targetfile.open("armadillo_results.txt");
	// inserting lower boundary conditions:
	targetfile << setw(15) << setprecision(8) << 0;
	targetfile << setw(15) << setprecision(8) << 0;
	targetfile << setw(15) << setprecision(8) << 0 << endl;

	for (int i = 0; i < n; i++){
		targetfile << setw(15) << setprecision(8) << x(i);
		targetfile << setw(15) << setprecision(8) << v(i);
		targetfile << setw(15) << setprecision(8) << v_anal(i) << endl;
	}

	//inserting upper boundary condions:
	targetfile << setw(15) << setprecision(8) << 1;
	targetfile << setw(15) << setprecision(8) << 0;
	targetfile << setw(15) << setprecision(8) << 0 << endl;

	targetfile.close();

	return 0;


}

double f(double x){
	return 100*exp(-10*x);
} // End: function f

double anal_solution(double x){
	return 1 - (1 - exp(-10))*x - exp(-10*x);
} // End: function anal_solution



