/********************************
 * Statistics
 * main.cpp
 * Created by Justin Leonard
********************************/

#include <iostream>
#include <vector>
#include "stats.h"

using namespace std;

int main ()
{
	// Variables
	int sub = 1;
	int r[9] = {1,2,3,4,5,6,7,8,9};
	int * pr = new int [9];
	vector<int> x1 (9);
	vector< vector<int> > x2;
	stats x;
	
	// Add to arrays
	for(int count = 0; count <= 8; count++)
	{
		x1[count] = sub;
		pr[count] = sub;
		sub++;
	}
	x2.push_back(x1);

	/* Test
	cout << x.Mean(r,9) << endl;
	cout << x.Mean(pr,9) << endl;
	cout << x.Mean(x1) << endl;
	cout << x.Mean(x2,0) << endl << endl;
	x.Mean(true);
	
	cout << x.Variance(r,9) << endl;
	cout << x.Variance(pr,9) << endl;
	cout << x.Variance(x1) << endl;
	cout << x.Variance(x2,0) << endl << endl;
	x.Variance(true);

	cout << x.StandardDev(r,9) << endl;
	cout << x.StandardDev(pr,9) << endl;
	cout << x.StandardDev(x1) << endl;
	cout << x.StandardDev(x2,0) << endl << endl;
	x.StandardDev(true);

	cout << x.MeanDev(r,9) << endl;
	cout << x.MeanDev(pr,9) << endl;
	cout << x.MeanDev(x1) << endl;
	cout << x.MeanDev(x2,0) << endl << endl;
	x.MeanDev(true);

	cout << x.LowerQuartile(r,9) << endl;
	cout << x.LowerQuartile(pr,9) << endl;
	cout << x.LowerQuartile(x1) << endl;
	cout << x.LowerQuartile(x2,0) << endl << endl;
	x.LowerQuartile(true);

	cout << x.Median(r,9) << endl;
	cout << x.Median(pr,9) << endl;
	cout << x.Median(x1) << endl;
	cout << x.Median(x2,0) << endl << endl;
	x.Median(true);

	cout << x.UpperQuartile(r,9) << endl;
	cout << x.UpperQuartile(pr,9) << endl;
	cout << x.UpperQuartile(x1) << endl;
	cout << x.UpperQuartile(x2,0) << endl << endl;
	x.UpperQuartile(true);

	cout << x.QuartileRange(r,9) << endl;
	cout << x.QuartileRange(pr,9) << endl;
	cout << x.QuartileRange(x1) << endl;
	cout << x.QuartileRange(x2,0) << endl << endl;
	x.QuartileRange(true);

	cout << x.Min(r,9) << endl;
	cout << x.Min(pr,9) << endl;
	cout << x.Min(x1) << endl;
	cout << x.Min(x2,0) << endl << endl;
	x.Min(true);

	cout << x.Max(r,9) << endl;
	cout << x.Max(pr,9) << endl;
	cout << x.Max(x1) << endl;
	cout << x.Max(x2,0) << endl << endl;
	x.Max(true);

	x.All(true);

	x.Decimal(2);

	x.Filename("data.txt");
	x.Target("output.txt");
	x.Input();
	x.Output();
	x.InputFile("test_in.txt");
	x.OutputFile("test_out.txt");
	x.ConsoleOutput();

	cout << Mean(x1) << "\n\n";
	cout << x.Mean(x1) << "\n\n";*/

	// Print to file
	x.InputFile("test_in.txt");

	// Delete array
	delete [] pr;

	// Return
	return 0;
}