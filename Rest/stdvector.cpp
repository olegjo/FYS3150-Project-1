#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<double> myVector;
	cout << "Vector size: " << myVector.size() << endl;
	myVector.resize(20);
	cout << "Vector size: " << myVector.size() << endl;
	myVector.push_back(12);

	cout << "Value: " << myVector.at(20) << endl;
	cout << "Value: " << myVector[20] << endl;

	cout << "Vector size: " << myVector.size() << endl;
	myVector.insert(myVector.begin(), 0);
	cout << "Vector size: " << myVector.size() << endl;
	return 0;
}