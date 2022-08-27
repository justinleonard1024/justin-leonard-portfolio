/********************************
 * Statistics
 * stats.h
 * Created by Justin Leonard
********************************/

#include <iostream>
#include <string>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <vector>

using namespace std;

// Class for main statistical analysis
class stats {
	public:
		// Main
		stats(void);
		~stats(void);

		// Statistics
		template<class T> double Mean(T *,int);
		template<class T> double Mean(std::vector< T >);
		template<class T> double Mean(std::vector< std::vector< T > >,int);

		template<class T> double Variance(T *,int);
		template<class T> double Variance(std::vector< T >);
		template<class T> double Variance(std::vector< std::vector< T > >,int);

		template<class T> double StandardDev(T *,int);
		template<class T> double StandardDev(std::vector< T >);
		template<class T> double StandardDev(std::vector< std::vector< T > >,int);

		template<class T> double MeanDev(T *,int);
		template<class T> double MeanDev(std::vector< T >);
		template<class T> double MeanDev(std::vector< std::vector< T > >,int);

		template<class T> double LowerQuartile(T *,int);
		template<class T> double LowerQuartile(std::vector< T >);
		template<class T> double LowerQuartile(std::vector< std::vector< T > >,int);

		template<class T> double Median(T *,int);
		template<class T> double Median(std::vector< T >);
		template<class T> double Median(std::vector< std::vector< T > >,int);

		template<class T> double UpperQuartile(T *,int);
		template<class T> double UpperQuartile(std::vector< T >);
		template<class T> double UpperQuartile(std::vector< std::vector< T > >,int);

		template<class T> double QuartileRange(T *,int);
		template<class T> double QuartileRange(std::vector< T >);
		template<class T> double QuartileRange(std::vector< std::vector< T > >,int);

		template<class T> double Min(T *,int);
		template<class T> double Min(std::vector< T >);
		template<class T> double Min(std::vector< std::vector< T > >,int);

		template<class T> double Max(T *,int);
		template<class T> double Max(std::vector< T >);
		template<class T> double Max(std::vector< std::vector< T > >,int);

		// Output Parameters
		void Mean(bool);
		void Variance(bool);
		void StandardDev(bool);
		void MeanDev(bool);
		void LowerQuartile(bool);
		void Median(bool);
		void UpperQuartile(bool);
		void QuartileRange(bool);
		void Min(bool);
		void Max(bool);
			
		void List(bool);
		void Decimal(int);
		void All(bool);

		// User data
		double Mean(void);
		double Variance(void);
		double StandardDev(void);
		double MeanDev(void);
		double LowerQuartile(void);
		double Median(void);
		double UpperQuartile(void);
		double QuartileRange(void);
		double Min(void);
		double Max(void);

		double Mean(int);
		double Variance(int);
		double StandardDev(int);
		double MeanDev(int);
		double LowerQuartile(int);
		double Median(int);
		double UpperQuartile(int);
		double QuartileRange(int);
		double Min(int);
		double Max(int);

		// File
		void Input(void);
		void Output(void);
		void InputFile(std::string);
		void OutputFile(std::string);
		void ConsoleOutput(void);
		void Filename(std::string);
		void Target(std::string);

		// Data
		template<class T> void Print(T *,int);
		template<class T> void Print(std::vector< T >);
		template<class T> void Print(std::vector< std::vector< T > >,int);

		template<class T> void Display(T *,int,int);
		template<class T> void Display(std::vector< T >,int);
		template<class T> void Display(std::vector< std::vector< T > >,int);

		template<class T> void Sort(T *&,int);
		template<class T> void Sort(std::vector< T >&);
		template<class T> void Sort(std::vector< std::vector< T > >&);

		void Clear(void);

	private:
		// Variables
		int amount, dec;
		bool setMean, setVariance, setStandardDev, setMeanDev,
			setLowerQuartile, setMedian, setUpperQuartile,
			setQuartileRange, setMin, setMax;
		bool setList, setInput, inFile, outFile, noData, error;
		std::string file, targ;
		std::ifstream file_input;
		std::ofstream file_output;
		std::vector< std::vector<double> > main_list;

		// Other
		bool isEven(int);

		// Error
		void errorInput(void);
		void errorOutput(void);
		void errorData(void);
		void errorValue(void);
};

// Constructor
stats::stats( void )
{
	setMean = true;
	setVariance = true;
	setStandardDev = true;
	setMeanDev = true;
	setLowerQuartile = true;
	setMedian = true;
	setUpperQuartile = true;
	setQuartileRange = true;
	setMin = true;
	setMax = true;
	setList = true;
	dec = 2;

	setInput = false;
	inFile = false;
	outFile = false;
	file = "";
	targ = "";
	
	noData = false;
	error = false;
}

// Destructor
stats::~stats( void )
{
	file_input.close();
	file_output.close();
}

// Mean

template<class T>
double stats::Mean(T * list,int size)
{
	double calc_mean = 0, calc_mean_temp = 0;

	for (int count = 0; count < size; count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= size;

	return calc_mean;
}

template<class T>
double stats::Mean(std::vector< T > list)
{
	double calc_mean = 0, calc_mean_temp = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list.size();

	return calc_mean;
}

template<class T>
double stats::Mean(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_mean = 0, calc_mean_temp = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_mean_temp = list[num][count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list[num].size();

	return calc_mean;
}

// Variance

template<class T>
double stats::Variance(T * list,int size)
{
	double calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (int count = 0; count < size; count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= size;
	
	for (int count = 0; count < size; count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= size;

	return calc_var;
}

template<class T>
double stats::Variance(std::vector< T > list)
{
	double calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list.size();
	
	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list.size();

	return calc_var;
}

template<class T>
double stats::Variance(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_mean = list[num][count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list[num].size();
	
	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_var = pow((list[num][count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list[num].size();

	return calc_var;
}

// Standard Deviation

template<class T>
double stats::StandardDev(T * list,int size)
{
	double calc_dev = 0, calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (int count = 0; count < size; count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= size;
	
	for (int count = 0; count < size; count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= size;

	calc_dev = sqrt(calc_var);

	return calc_dev;
}

template<class T>
double stats::StandardDev(std::vector< T > list)
{
	double calc_dev = 0, calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list.size();
	
	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list.size();

	calc_dev = sqrt(calc_var);

	return calc_dev;
}

template<class T>
double stats::StandardDev(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_dev = 0, calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_mean = list[num][count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list[num].size();
	
	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_var = pow((list[num][count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list[num].size();

	calc_dev = sqrt(calc_var);

	return calc_dev;
}

// Mean Deviation

template<class T>
double stats::MeanDev(T * list,int size)
{
	double calc_mean = 0, calc_mean_temp = 0;
	double calc_dev = 0, calc_dev_temp = 0;

	for (int count = 0; count < size; count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= size;

	for (int count = 0; count < size; count++)
	{
		calc_dev_temp = abs(calc_mean - list[count]);
		calc_dev += calc_dev_temp;
	}
	calc_dev /= size;

	return calc_dev;
}

template<class T>
double stats::MeanDev(std::vector< T > list)
{
	double calc_mean = 0, calc_mean_temp = 0;
	double calc_dev = 0, calc_dev_temp = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list.size();

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_dev_temp = abs(calc_mean - list[count]);
		calc_dev += calc_dev_temp;
	}
	calc_dev /= list.size();

	return calc_dev;
}

template<class T>
double stats::MeanDev(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_mean = 0, calc_mean_temp = 0;
	double calc_dev = 0, calc_dev_temp = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_mean_temp = list[num][count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list[num].size();

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_dev_temp = abs(calc_mean - list[num][count]);
		calc_dev += calc_dev_temp;
	}
	calc_dev /= list[num].size();

	return calc_dev;
}

// Lower Quartile

template<class T>
double stats::LowerQuartile(T * list,int size)
{
	int calc_mid = (size / 2) - 1, calc_mid_quarter = (size / 4) - 1;
	int calc_mid_real = (size / 2), calc_mid_quarter_real = (size / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(size);
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((size - 1) / 2);

	if(size >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[calc_mid_quarter] + list[calc_mid_quarter + 1]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid - (calc_mid_quarter + 1)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid - (calc_mid_quarter)] + list[calc_mid - (calc_mid_quarter + 1)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid_quarter_real];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(size == 3)
	{
		calc_spec_quartile = (list[0] + list[1]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double stats::LowerQuartile(std::vector< T > list)
{
	int calc_mid = (list.size() / 2) - 1, calc_mid_quarter = (list.size() / 4) - 1;
	int calc_mid_real = (list.size() / 2), calc_mid_quarter_real = (list.size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list.size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list.size() - 1) / 2);

	if(list.size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[calc_mid_quarter] + list[calc_mid_quarter + 1]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid - (calc_mid_quarter + 1)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid - (calc_mid_quarter)] + list[calc_mid - (calc_mid_quarter + 1)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid_quarter_real];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list.size() == 3)
	{
		calc_spec_quartile = (list[0] + list[1]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double stats::LowerQuartile(std::vector< std::vector< T > > list,int num = 0)
{
	int calc_mid = (list[num].size() / 2) - 1, calc_mid_quarter = (list[num].size() / 4) - 1;
	int calc_mid_real = (list[num].size() / 2), calc_mid_quarter_real = (list[num].size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list[num].size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list[num].size() - 1) / 2);

	if(list[num].size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[num][calc_mid_quarter] + list[num][calc_mid_quarter + 1]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[num][calc_mid - (calc_mid_quarter + 1)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[num][calc_mid - (calc_mid_quarter)] + list[num][calc_mid - (calc_mid_quarter + 1)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[num][calc_mid_quarter_real];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list[num].size() == 3)
	{
		calc_spec_quartile = (list[num][0] + list[num][1]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	
	return calc_quartile;
}

// Median

template<class T>
double stats::Median(T * list,int size)
{
	int calc_mid = (size / 2) - 1, calc_mid_quarter = (size / 4) - 1;
	int calc_mid_real = (size / 2), calc_mid_quarter_real = (size / 4);
	double calc_median, calc_mid_even, calc_mid_odd, calc_mid_spec;
	bool num_test = isEven(size);

	if(size >= 4)
	{
		if(num_test == true)
		{
			calc_mid_even = (list[calc_mid + 1] + list[calc_mid]) / 2.0;
			calc_median = calc_mid_even;
		}
		else
		{
			calc_mid_odd = list[calc_mid_real];
			calc_median = calc_mid_odd;
		}
	}
	else if(size == 3)
	{
		calc_mid_spec = calc_mid;
		calc_median = calc_mid_spec;
	}
	else if(size == 2)
	{
		calc_mid_spec = (list[0] + list[1]) / 2.0;
		calc_median = calc_mid_spec;
	}
	else if(size == 1)
	{
		calc_mid_spec = list[0];
		calc_median = calc_mid_spec;
	}

	return calc_median;
}

template<class T>
double stats::Median(std::vector< T > list)
{
	int calc_mid = (list.size() / 2) - 1, calc_mid_quarter = (list.size() / 4) - 1;
	int calc_mid_real = (list.size() / 2), calc_mid_quarter_real = (list.size() / 4);
	double calc_median, calc_mid_even, calc_mid_odd, calc_mid_spec;
	bool num_test = isEven(list.size());

	if(list.size() >= 4)
	{
		if(num_test == true)
		{
			calc_mid_even = (list[calc_mid + 1] + list[calc_mid]) / 2.0;
			calc_median = calc_mid_even;
		}
		else
		{
			calc_mid_odd = list[calc_mid_real];
			calc_median = calc_mid_odd;
		}
	}
	else if(list.size() == 3)
	{
		calc_mid_spec = calc_mid;
		calc_median = calc_mid_spec;
	}
	else if(list.size() == 2)
	{
		calc_mid_spec = (list[0] + list[1]) / 2.0;
		calc_median = calc_mid_spec;
	}
	else if(list.size() == 1)
	{
		calc_mid_spec = list[0];
		calc_median = calc_mid_spec;
	}

	return calc_median;
}

template<class T>
double stats::Median(std::vector< std::vector< T > > list,int num = 0)
{
	int calc_mid = (list[num].size() / 2) - 1, calc_mid_quarter = (list[num].size() / 4) - 1;
	int calc_mid_real = (list[num].size() / 2), calc_mid_quarter_real = (list[num].size() / 4);
	double calc_median, calc_mid_even, calc_mid_odd, calc_mid_spec;
	bool num_test = isEven(list[num].size());

	if(list[num].size() >= 4)
	{
		if(num_test == true)
		{
			calc_mid_even = (list[num][calc_mid + 1] + list[num][calc_mid]) / 2.0;
			calc_median = calc_mid_even;
		}
		else
		{
			calc_mid_odd = list[num][calc_mid_real];
			calc_median = calc_mid_odd;
		}
	}
	else if(list[num].size() == 3)
	{
		calc_mid_spec = calc_mid;
		calc_median = calc_mid_spec;
	}
	else if(list[num].size() == 2)
	{
		calc_mid_spec = (list[num][0] + list[num][1]) / 2.0;
		calc_median = calc_mid_spec;
	}
	else if(list[num].size() == 1)
	{
		calc_mid_spec = list[num][0];
		calc_median = calc_mid_spec;
	}

	return calc_median;
}

// Upper Quartile

template<class T>
double stats::UpperQuartile(T * list,int size)
{
	int calc_mid = (size / 2) - 1, calc_mid_quarter = (size / 4) - 1;
	int calc_mid_real = (size / 2), calc_mid_quarter_real = (size / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(size);
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((size - 1) / 2);
		
	if(size >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[(calc_mid + calc_mid_quarter) + 1] + list[(calc_mid + calc_mid_quarter) + 2]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid + (calc_mid_quarter + 2)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid + (calc_mid_quarter_real + 1)] + list[calc_mid + (calc_mid_quarter_real + 2)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid + (calc_mid_quarter_real + 2)];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(size == 3)
	{
		calc_spec_quartile = (list[1] + list[2]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double stats::UpperQuartile(std::vector< T > list)
{
	int calc_mid = (list.size() / 2) - 1, calc_mid_quarter = (list.size() / 4) - 1;
	int calc_mid_real = (list.size() / 2), calc_mid_quarter_real = (list.size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list.size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list.size() - 1) / 2);
		
	if(list.size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[(calc_mid + calc_mid_quarter) + 1] + list[(calc_mid + calc_mid_quarter) + 2]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid + (calc_mid_quarter + 2)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid + (calc_mid_quarter_real + 1)] + list[calc_mid + (calc_mid_quarter_real + 2)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid + (calc_mid_quarter_real + 2)];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list.size() == 3)
	{
		calc_spec_quartile = (list[1] + list[2]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double stats::UpperQuartile(std::vector< std::vector< T > > list,int num = 0)
{
	int calc_mid = (list[num].size() / 2) - 1, calc_mid_quarter = (list[num].size() / 4) - 1;
	int calc_mid_real = (list[num].size() / 2), calc_mid_quarter_real = (list[num].size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list[num].size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list[num].size() - 1) / 2);
	
	if(list[num].size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[num][(calc_mid + calc_mid_quarter) + 1] + list[num][(calc_mid + calc_mid_quarter) + 2]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[num][calc_mid + (calc_mid_quarter + 2)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[num][calc_mid + (calc_mid_quarter_real + 1)] + list[num][calc_mid + (calc_mid_quarter_real + 2)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[num][calc_mid + (calc_mid_quarter_real + 2)];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list[num].size() == 3)
	{
		calc_spec_quartile = (list[num][1] + list[num][2]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	
	return calc_quartile;
}

// Interquartile Range

template<class T>
double stats::QuartileRange(T * list,int size)
{
	double calc_range, calc_quartile_lower, calc_quartile_upper;

	calc_quartile_lower = LowerQuartile(list,size);
	calc_quartile_upper = UpperQuartile(list,size);

	calc_range = calc_quartile_upper - calc_quartile_lower;

	return calc_range;
}

template<class T>
double stats::QuartileRange(std::vector< T > list)
{
	double calc_range, calc_quartile_lower, calc_quartile_upper;

	calc_quartile_lower = LowerQuartile(list);
	calc_quartile_upper = UpperQuartile(list);

	calc_range = calc_quartile_upper - calc_quartile_lower;

	return calc_range;
}

template<class T>
double stats::QuartileRange(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_range, calc_quartile_lower, calc_quartile_upper;

	calc_quartile_lower = LowerQuartile(list,num);
	calc_quartile_upper = UpperQuartile(list,num);

	calc_range = calc_quartile_upper - calc_quartile_lower;

	return calc_range;
}

// Minimum

template<class T>
double stats::Min(T * list,int size)
{
	double calc_min, calc_min_temp = list[0];

	for(int count = 0; count < size; count++)
	{
		if(list[count] < calc_min_temp)
		{
			calc_min_temp = list[count];
		}
	}

	calc_min = calc_min_temp;

	return calc_min;
}

template<class T>
double stats::Min(std::vector< T > list)
{
	double calc_min, calc_min_temp = list[0];

	for(unsigned int count = 0; count < list.size(); count++)
	{
		if(list[count] < calc_min_temp)
		{
			calc_min_temp = list[count];
		}
	}

	calc_min = calc_min_temp;

	return calc_min;
}

template<class T>
double stats::Min(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_min, calc_min_temp = list[num][0];

	for(unsigned int count = 0; count < list[num].size(); count++)
	{
		if(list[num][count] < calc_min_temp)
		{
			calc_min_temp = list[num][count];
		}
	}

	calc_min = calc_min_temp;

	return calc_min;
}

// Maximum

template<class T>
double stats::Max(T * list,int size)
{
	double calc_max, calc_max_temp = list[0];

	for(int count = 0; count < size; count++)
	{
		if(list[count] > calc_max_temp)
		{
			calc_max_temp = list[count];
		}
	}

	calc_max = calc_max_temp;

	return calc_max;
}

template<class T>
double stats::Max(std::vector< T > list)
{
	double calc_max, calc_max_temp = list[0];

	for(unsigned int count = 0; count < list.size(); count++)
	{
		if(list[count] > calc_max_temp)
		{
			calc_max_temp = list[count];
		}
	}

	calc_max = calc_max_temp;

	return calc_max;
}

template<class T>
double stats::Max(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_max, calc_max_temp = list[num][0];

	for(unsigned int count = 0; count < list[num].size(); count++)
	{
		if(list[num][count] > calc_max_temp)
		{
			calc_max_temp = list[num][count];
		}
	}

	calc_max = calc_max_temp;

	return calc_max;
}

// Output Parameters

void stats::Mean(bool _set)
{
	bool temp = _set;
	setMean = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::Variance(bool _set)
{
	bool temp = _set;
	setVariance = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::StandardDev(bool _set)
{
	bool temp = _set;
	setStandardDev = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::MeanDev(bool _set)
{
	bool temp = _set;
	setMeanDev = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::LowerQuartile(bool _set)
{
	bool temp = _set;
	setLowerQuartile = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::Median(bool _set)
{
	bool temp = _set;
	setMedian = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::UpperQuartile(bool _set)
{
	bool temp = _set;
	setUpperQuartile = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::QuartileRange(bool _set)
{
	bool temp = _set;
	setQuartileRange = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::Min(bool _set)
{
	bool temp = _set;
	setMin = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::Max(bool _set)
{
	bool temp = _set;
	setMax = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::List(bool _set)
{
	bool temp = _set;
	setList = temp;

	if(temp == true)
	{
		noData = false;
	}
}

void stats::Decimal(int _set)
{
	int temp = _set;
	dec = temp;
}

void stats::All(bool _set)
{
	bool temp = _set;
		
	setMean = temp;
	setVariance = temp;
	setStandardDev = temp;
	setMeanDev = temp;
	setLowerQuartile = temp;
	setMedian = temp;
	setUpperQuartile = temp;
	setQuartileRange = temp;
	setMin = temp;
	setMax = temp;
	setList = temp;

	noData = !temp;
}

// User data

double stats::Mean( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = Mean(main_list,0);
		return temp;
	}
}

double stats::Variance( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = Variance(main_list,0);
		return temp;
	}
}

double stats::StandardDev( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = StandardDev(main_list,0);
		return temp;
	}
}

double stats::MeanDev( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = MeanDev(main_list,0);
		return temp;
	}
}

double stats::LowerQuartile( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = LowerQuartile(main_list,0);
		return temp;
	}
}

double stats::Median( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = Median(main_list,0);
		return temp;
	}
}

double stats::UpperQuartile( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = UpperQuartile(main_list,0);
		return temp;
	}
}

double stats::QuartileRange( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = QuartileRange(main_list,0);
		return temp;
	}
}

double stats::Min( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = Min(main_list,0);
		return temp;
	}
}

double stats::Max( void )
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		temp = Max(main_list,0);
		return temp;
	}
}

double stats::Mean(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = Mean(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::Variance(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = Variance(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::StandardDev(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = StandardDev(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::MeanDev(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = MeanDev(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::LowerQuartile(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = LowerQuartile(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::Median(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = Median(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::UpperQuartile(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = UpperQuartile(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::QuartileRange(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = QuartileRange(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::Min(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = Min(main_list,(num - 1));
			return temp;
		}
	}
}

double stats::Max(int num)
{
	double temp;

	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		if(num <= 0 || num > amount)
		{
			errorValue();
			exit(1);
		}
		else
		{
			temp = Max(main_list,(num - 1));
			return temp;
		}
	}
}

// Input and output

void stats::Input( void )
{
	if(inFile == false)
	{
		errorInput();
		exit(1);
	}
	else
	{
		setInput = true;
	
		file_input.open(file);
		if(!file_input)
		{
			cout << endl << "--------------------------------";
			cout << endl << endl;
			cout << "File open failure!";
			cout << endl << endl;
			cout << "--------------------------------" << endl << endl;
			exit(1);
		}

		file_input >> amount;

		for (int count = 0; count < amount; count++)
		{
			int calc_amt;
			file_input >> calc_amt;

			vector<double> row;
			for (int sub = 0; sub < calc_amt; sub++) 
			{
				row.push_back(count * sub);
			}
			main_list.push_back(row);

			for (int sub = 0; sub < calc_amt; sub++) 
			{
				file_input >> main_list[count][sub];
			}
		}

		file_input.close();
	}
}

void stats::Output( void )
{
	if(outFile == false)
	{
		errorOutput();
		exit(1);
	}
	else
	{
		if(setInput == false)
		{
			errorData();
			exit(1);
		}
		else
		{
			file_output.open(targ);
			if(!file_output)
			{
				cout << endl << "--------------------------------";
				cout << endl << endl;
				cout << "File open failure!";
				cout << endl << endl;
				cout << "--------------------------------" << endl << endl;
				exit(1);
			}

			file_output << setprecision(dec) << fixed;

			for(int count = 0; count < amount; count++)
			{
				file_output << endl << endl << endl;
				file_output << "--------------------------------";
				file_output << endl << endl << endl << endl;
				file_output << "Data Set " << (count + 1);
				file_output << endl << endl << endl;
					
				if(noData == true)
				{
					file_output << "The is no data" << endl;
				}
				else
				{
					Sort(main_list);

					if(setList == true)
						Print(main_list,count);
					
					if(setMean == true)
						file_output << "The mean of the data is " << Mean(main_list,count) << endl;

					if(setVariance == true)
						file_output << "The variance of the data is " << Variance(main_list,count) << endl;

					if(setStandardDev == true)
						file_output << "The standard deviation of the data is " << StandardDev(main_list,count) << endl;

					if(setMeanDev == true)
						file_output << "The mean deviation of the data is " << MeanDev(main_list,count) << endl;

					if((setMean || setVariance || setStandardDev || setMeanDev) && (setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange))
						file_output << endl;

					if((setMean || setVariance || setStandardDev || setMeanDev) && !(setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange) && (setMin || setMax))
						file_output << endl;

					if(setLowerQuartile == true)
						file_output << "The lower quartile of the data is " << LowerQuartile(main_list,count) << endl;

					if(setMedian == true)
						file_output << "The median of the data is " << Median(main_list,count) << endl;
						
					if(setUpperQuartile == true)
						file_output << "The upper quartile of the data is " << UpperQuartile(main_list,count) << endl;

					if(setQuartileRange == true)
						file_output << "The interquartile range of the data is " << QuartileRange(main_list,count) << endl;

					if((setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange) && (setMin || setMax))
						file_output << endl;

					if(setMin == true)
						file_output << "The minimum of the data is " << Min(main_list,count) << endl;

					if(setMax == true)
						file_output << "The maximum of the data is " << Max(main_list,count) << endl;
				}
			}

			file_output << endl << endl << endl;
			file_output << "--------------------------------";
			file_output << endl << endl << endl;

			file_output.close();
		}
	}
}

void stats::InputFile(std::string _file)
{
	setInput = true;
	
	file_input.open(_file);
	if(!file_input)
	{
		cout << endl << "--------------------------------";
		cout << endl << endl;
		cout << "File open failure!";
		cout << endl << endl;
		cout << "--------------------------------" << endl << endl;
		exit(1);
	}

	file_input >> amount;

	for (int count = 0; count < amount; count++)
	{
		int calc_amt;
		file_input >> calc_amt;

		vector<double> row;
		for (int sub = 0; sub < calc_amt; sub++) 
		{
			row.push_back(count * sub);
		}
		main_list.push_back(row);

		for (int sub = 0; sub < calc_amt; sub++) 
		{
			file_input >> main_list[count][sub];
		}
	}

	file_input.close();
}

void stats::OutputFile(std::string _file)
{
	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		file_output.open(_file);
		if(!file_output)
		{
			cout << endl << "--------------------------------";
			cout << endl << endl;
			cout << "File open failure!";
			cout << endl << endl;
			cout << "--------------------------------" << endl << endl;
			exit(1);
		}

		file_output << setprecision(dec) << fixed;

		for(int count = 0; count < amount; count++)
		{
			file_output << endl << endl << endl;
			file_output << "--------------------------------";
			file_output << endl << endl << endl << endl;
			file_output << "Data Set " << (count + 1);
			file_output << endl << endl << endl;
					
			if(noData == true)
			{
				file_output << "The is no data" << endl;
			}
			else
			{
				Sort(main_list);

				if(setList == true)
					Print(main_list,count);
					
				if(setMean == true)
					file_output << "The mean of the data is " << Mean(main_list,count) << endl;

				if(setVariance == true)
					file_output << "The variance of the data is " << Variance(main_list,count) << endl;

				if(setStandardDev == true)
					file_output << "The standard deviation of the data is " << StandardDev(main_list,count) << endl;

				if(setMeanDev == true)
					file_output << "The mean deviation of the data is " << MeanDev(main_list,count) << endl;

				if((setMean || setVariance || setStandardDev || setMeanDev) && (setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange))
					file_output << endl;

				if((setMean || setVariance || setStandardDev || setMeanDev) && !(setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange) && (setMin || setMax))
					file_output << endl;

				if(setLowerQuartile == true)
					file_output << "The lower quartile of the data is " << LowerQuartile(main_list,count) << endl;

				if(setMedian == true)
					file_output << "The median of the data is " << Median(main_list,count) << endl;
						
				if(setUpperQuartile == true)
					file_output << "The upper quartile of the data is " << UpperQuartile(main_list,count) << endl;

				if(setQuartileRange == true)
					file_output << "The interquartile range of the data is " << QuartileRange(main_list,count) << endl;

				if((setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange) && (setMin || setMax))
					file_output << endl;

				if(setMin == true)
					file_output << "The minimum of the data is " << Min(main_list,count) << endl;

				if(setMax == true)
					file_output << "The maximum of the data is " << Max(main_list,count) << endl;
			}
		}

		file_output << endl << endl << endl;
		file_output << "--------------------------------";
		file_output << endl << endl << endl;

		file_output.close();
	}
}

void stats::ConsoleOutput( void )
{
	if(setInput == false)
	{
		errorData();
		exit(1);
	}
	else
	{
		cout << setprecision(dec) << fixed;

		for(int count = 0; count < amount; count++)
		{
			cout << endl << endl << endl;
			cout << "--------------------------------";
			cout << endl << endl << endl << endl;
			cout << "Data Set " << (count + 1);
			cout << endl << endl << endl;
					
			if(noData == true)
			{
				cout << "The is no data" << endl;
			}
			else
			{
				Sort(main_list);

				if(setList == true)
					Display(main_list,count);
					
				if(setMean == true)
					cout << "The mean of the data is " << Mean(main_list,count) << endl;

				if(setVariance == true)
					cout << "The variance of the data is " << Variance(main_list,count) << endl;

				if(setStandardDev == true)
					cout << "The standard deviation of the data is " << StandardDev(main_list,count) << endl;

				if(setMeanDev == true)
					cout << "The mean deviation of the data is " << MeanDev(main_list,count) << endl;

				if((setMean || setVariance || setStandardDev || setMeanDev) && (setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange))
					cout << endl;

				if((setMean || setVariance || setStandardDev || setMeanDev) && !(setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange) && (setMin || setMax))
					cout << endl;

				if(setLowerQuartile == true)
					cout << "The lower quartile of the data is " << LowerQuartile(main_list,count) << endl;

				if(setMedian == true)
					cout << "The median of the data is " << Median(main_list,count) << endl;
						
				if(setUpperQuartile == true)
					cout << "The upper quartile of the data is " << UpperQuartile(main_list,count) << endl;

				if(setQuartileRange == true)
					cout << "The interquartile range of the data is " << QuartileRange(main_list,count) << endl;

				if((setLowerQuartile || setMedian || setUpperQuartile || setQuartileRange) && (setMin || setMax))
					cout << endl;

				if(setMin == true)
					cout << "The minimum of the data is " << Min(main_list,count) << endl;

				if(setMax == true)
					cout << "The maximum of the data is " << Max(main_list,count) << endl;
			}
		}

		cout << endl << endl << endl;
		cout << "--------------------------------";
		cout << endl << endl << endl;
	}
}

// File Name

void stats::Filename(std::string _file)
{
	string temp_file = _file;
	file = temp_file;
		
	if (temp_file != "")
	{
		inFile = true;
	}
}

void stats::Target(std::string _file)
{
	string temp_file = _file;
	targ = temp_file;
		
	if (temp_file != "")
	{
		outFile = true;
	}
}

// Data
	
template<class T>
void stats::Print(T * list,int size)
{
	int count_line = 1;

	file_output << "Data List" << endl << endl;
   
	for(unsigned int count = 0; count <= (size - 1); count++)
	{
		count_line++;
		if(count_line <= 5)
		{
			file_output << right << list[count] << setw(20);
		}
		else
		{
			file_output << right << list[count] << endl;
			count_line = 1;
		}
	}
	
	file_output << endl << endl;
}

template<class T>
void stats::Print(std::vector< T > list)
{
	int count_line = 1;

	file_output << "Data List" << endl << endl;
   
	for(unsigned int count = 0; count <= (list.size() - 1); count++)
	{
		count_line++;
		if(count_line <= 5)
		{
			file_output << right << list[count] << setw(20);
		}
		else
		{
			file_output << right << list[count] << endl;
			count_line = 1;
		}
	}
	
	file_output << endl << endl;
}

template<class T>
void stats::Print(std::vector< std::vector< T > > list,int num = 0)
{
	int count_line = 1;

	file_output << "Data List" << endl << endl;
   
	for(unsigned int count = 0; count <= (list[num].size() - 1); count++)
	{
		count_line++;
		if(count_line <= 5)
		{
			file_output << right << list[num][count] << setw(20);
		}
		else
		{
			file_output << right << list[num][count] << endl;
			count_line = 1;
		}
	}
	
	file_output << endl << endl;
}

template<class T>
void stats::Display(T * list,int size,int dataset = 0)
{
	int count_line = 1;

	cout << endl << endl << endl;
	cout << "Data List " << (dataset + 1) << endl << endl;
   
	for(unsigned int count = 0; count <= (size - 1); count++)
	{
		count_line++;
		if(count_line <= 5)
		{
			cout << right << list[count] << setw(5);
		}
		else
		{
			cout << right << list[count] << endl;
			count_line = 1;
		}
	}

	cout << endl << endl;
}

template<class T>
void stats::Display(std::vector< T > list,int dataset = 0)
{
	int count_line = 1;

	cout << endl << endl << endl;
	cout << "Data List " << (dataset + 1) << endl << endl;
   
	for(unsigned int count = 0; count <= (list.size() - 1); count++)
	{
		count_line++;
		if(count_line <= 5)
		{
			cout << right << list[count] << setw(5);
		}
		else
		{
			cout << right << list[count] << endl;
			count_line = 1;
		}
	}

	cout << endl << endl;
}

template<class T>
void stats::Display(std::vector< std::vector< T > > list,int dataset = 0)
{
	int count_line = 1;

	cout << endl << endl << endl;
	cout << "Data List " << (dataset + 1) << endl << endl;
   
	for(unsigned int count = 0; count <= (list[dataset].size() - 1); count++)
	{
		count_line++;
		if(count_line <= 5)
		{
			cout << right << list[dataset][count] << setw(5);
		}
		else
		{
			cout << right << list[dataset][count] << endl;
			count_line = 1;
		}
	}

	cout << endl << endl;
}

template<class T>
void stats::Sort(T * &list,int size)
{
	bool swap;
	double temp;

	do
	{
		swap = false;

		for (unsigned int sub = 0; sub < (size - 1); sub++)
		{
			if (list[sub] > list[sub + 1])
			{
				temp = list[sub];
				list[sub] = list[sub + 1];
				list[sub + 1] = temp;

				swap = true;
			}
		}
	} while (swap);
}

template<class T>
void stats::Sort(std::vector< T >& list)
{
	bool swap;
	double temp;

	do
	{
		swap = false;

		for (unsigned int sub = 0; sub < (list.size() - 1); sub++)
		{
			if (list[sub] > list[sub + 1])
			{
				temp = list[sub];
				list[sub] = list[sub + 1];
				list[sub + 1] = temp;

				swap = true;
			}
		}
	} while (swap);
}

template<class T>
void stats::Sort(std::vector< std::vector< T > >& list)
{
	bool swap;
	double temp;

	for(unsigned int count = 0; count < list.size(); count++)
	{
		do
		{
			swap = false;

			for (unsigned int sub = 0; sub < (list[count].size() - 1); sub++)
			{
				if (list[count][sub] > list[count][sub + 1])
				{
					temp = list[count][sub];
					list[count][sub] = list[count][sub + 1];
					list[count][sub + 1] = temp;

					swap = true;
				}
			}
		} while (swap);
	}
}

void stats::Clear( void )
{
	setInput = false;
	main_list.clear();
}

// Other

bool stats::isEven(int num)
{
	if ( (num % 2) == 0 )
	{
		return true;
	}
	else
	{
		return false;
	}
}

// Error

void stats::errorInput( void )
{
	error = true;

	system("cls");

	cout << endl << "--------------------------------";
	cout << endl << endl;
	cout << "Error:  There is no input file name";
	cout << endl << endl;
	cout << "--------------------------------" << endl << endl;
}

void stats::errorOutput( void )
{
	error = true;
		
	system("cls");

	cout << endl << "--------------------------------";
	cout << endl << endl;
	cout << "Error:  There is no output file name";
	cout << endl << endl;
	cout << "--------------------------------" << endl << endl;
}

void stats::errorData( void )
{
	error = true;
		
	system("cls");

	cout << endl << "--------------------------------";
	cout << endl << endl;
	cout << "Error:  There is no input data";
	cout << endl << endl;
	cout << "--------------------------------" << endl << endl;
}

void stats::errorValue( void )
{
	error = true;
		
	system("cls");

	cout << endl << "--------------------------------";
	cout << endl << endl;
	cout << "Error:  The selected value is not valid";
	cout << endl << endl;
	cout << "--------------------------------" << endl << endl;
}

// Independent Functions

// Mean

template<class T>
double Mean(T * list,int size)
{
	double calc_mean = 0, calc_mean_temp = 0;

	for (int count = 0; count < size; count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= size;

	return calc_mean;
}

template<class T>
double Mean(std::vector< T > list)
{
	double calc_mean = 0, calc_mean_temp = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list.size();

	return calc_mean;
}

template<class T>
double Mean(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_mean = 0, calc_mean_temp = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_mean_temp = list[num][count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list[num].size();

	return calc_mean;
}

// Variance

template<class T>
double Variance(T * list,int size)
{
	double calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (int count = 0; count < size; count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= size;
	
	for (int count = 0; count < size; count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= size;

	return calc_var;
}

template<class T>
double Variance(std::vector< T > list)
{
	double calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list.size();
	
	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list.size();

	return calc_var;
}

template<class T>
double Variance(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_mean = list[num][count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list[num].size();
	
	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_var = pow((list[num][count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list[num].size();

	return calc_var;
}

// Standard Deviation

template<class T>
double StandardDev(T * list,int size)
{
	double calc_dev = 0, calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (int count = 0; count < size; count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= size;
	
	for (int count = 0; count < size; count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= size;

	calc_dev = sqrt(calc_var);

	return calc_dev;
}

template<class T>
double StandardDev(std::vector< T > list)
{
	double calc_dev = 0, calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_mean = list[count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list.size();
	
	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_temp_var = pow((list[count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list.size();

	calc_dev = sqrt(calc_var);

	return calc_dev;
}

template<class T>
double StandardDev(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_dev = 0, calc_var = 0, calc_mean = 0, calc_temp_var = 0, calc_temp_mean = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_mean = list[num][count];
		calc_mean += calc_temp_mean;
	}
	calc_mean /= list[num].size();
	
	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_temp_var = pow((list[num][count] - calc_mean),2);
		calc_var += calc_temp_var;
	}
	calc_var /= list[num].size();

	calc_dev = sqrt(calc_var);

	return calc_dev;
}

// Mean Deviation

template<class T>
double MeanDev(T * list,int size)
{
	double calc_mean = 0, calc_mean_temp = 0;
	double calc_dev = 0, calc_dev_temp = 0;

	for (int count = 0; count < size; count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= size;

	for (int count = 0; count < size; count++)
	{
		calc_dev_temp = abs(calc_mean - list[count]);
		calc_dev += calc_dev_temp;
	}
	calc_dev /= size;

	return calc_dev;
}

template<class T>
double MeanDev(std::vector< T > list)
{
	double calc_mean = 0, calc_mean_temp = 0;
	double calc_dev = 0, calc_dev_temp = 0;

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_mean_temp = list[count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list.size();

	for (unsigned int count = 0; count < list.size(); count++)
	{
		calc_dev_temp = abs(calc_mean - list[count]);
		calc_dev += calc_dev_temp;
	}
	calc_dev /= list.size();

	return calc_dev;
}

template<class T>
double MeanDev(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_mean = 0, calc_mean_temp = 0;
	double calc_dev = 0, calc_dev_temp = 0;

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_mean_temp = list[num][count];
		calc_mean += calc_mean_temp;
	}
	calc_mean /= list[num].size();

	for (unsigned int count = 0; count < list[num].size(); count++)
	{
		calc_dev_temp = abs(calc_mean - list[num][count]);
		calc_dev += calc_dev_temp;
	}
	calc_dev /= list[num].size();

	return calc_dev;
}

// Lower Quartile

template<class T>
double LowerQuartile(T * list,int size)
{
	int calc_mid = (size / 2) - 1, calc_mid_quarter = (size / 4) - 1;
	int calc_mid_real = (size / 2), calc_mid_quarter_real = (size / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(size);
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((size - 1) / 2);

	if(size >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[calc_mid_quarter] + list[calc_mid_quarter + 1]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid - (calc_mid_quarter + 1)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid - (calc_mid_quarter)] + list[calc_mid - (calc_mid_quarter + 1)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid_quarter_real];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(size == 3)
	{
		calc_spec_quartile = (list[0] + list[1]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double LowerQuartile(std::vector< T > list)
{
	int calc_mid = (list.size() / 2) - 1, calc_mid_quarter = (list.size() / 4) - 1;
	int calc_mid_real = (list.size() / 2), calc_mid_quarter_real = (list.size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list.size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list.size() - 1) / 2);

	if(list.size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[calc_mid_quarter] + list[calc_mid_quarter + 1]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid - (calc_mid_quarter + 1)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid - (calc_mid_quarter)] + list[calc_mid - (calc_mid_quarter + 1)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid_quarter_real];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list.size() == 3)
	{
		calc_spec_quartile = (list[0] + list[1]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double LowerQuartile(std::vector< std::vector< T > > list,int num = 0)
{
	int calc_mid = (list[num].size() / 2) - 1, calc_mid_quarter = (list[num].size() / 4) - 1;
	int calc_mid_real = (list[num].size() / 2), calc_mid_quarter_real = (list[num].size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list[num].size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list[num].size() - 1) / 2);

	if(list[num].size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[num][calc_mid_quarter] + list[num][calc_mid_quarter + 1]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[num][calc_mid - (calc_mid_quarter + 1)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[num][calc_mid - (calc_mid_quarter)] + list[num][calc_mid - (calc_mid_quarter + 1)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[num][calc_mid_quarter_real];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list[num].size() == 3)
	{
		calc_spec_quartile = (list[num][0] + list[num][1]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	
	return calc_quartile;
}

// Median

template<class T>
double Median(T * list,int size)
{
	int calc_mid = (size / 2) - 1, calc_mid_quarter = (size / 4) - 1;
	int calc_mid_real = (size / 2), calc_mid_quarter_real = (size / 4);
	double calc_median, calc_mid_even, calc_mid_odd, calc_mid_spec;
	bool num_test = isEven(size);

	if(size >= 4)
	{
		if(num_test == true)
		{
			calc_mid_even = (list[calc_mid + 1] + list[calc_mid]) / 2.0;
			calc_median = calc_mid_even;
		}
		else
		{
			calc_mid_odd = list[calc_mid_real];
			calc_median = calc_mid_odd;
		}
	}
	else if(size == 3)
	{
		calc_mid_spec = calc_mid;
		calc_median = calc_mid_spec;
	}
	else if(size == 2)
	{
		calc_mid_spec = (list[0] + list[1]) / 2.0;
		calc_median = calc_mid_spec;
	}
	else if(size == 1)
	{
		calc_mid_spec = list[0];
		calc_median = calc_mid_spec;
	}

	return calc_median;
}

template<class T>
double Median(std::vector< T > list)
{
	int calc_mid = (list.size() / 2) - 1, calc_mid_quarter = (list.size() / 4) - 1;
	int calc_mid_real = (list.size() / 2), calc_mid_quarter_real = (list.size() / 4);
	double calc_median, calc_mid_even, calc_mid_odd, calc_mid_spec;
	bool num_test = isEven(list.size());

	if(list.size() >= 4)
	{
		if(num_test == true)
		{
			calc_mid_even = (list[calc_mid + 1] + list[calc_mid]) / 2.0;
			calc_median = calc_mid_even;
		}
		else
		{
			calc_mid_odd = list[calc_mid_real];
			calc_median = calc_mid_odd;
		}
	}
	else if(list.size() == 3)
	{
		calc_mid_spec = calc_mid;
		calc_median = calc_mid_spec;
	}
	else if(list.size() == 2)
	{
		calc_mid_spec = (list[0] + list[1]) / 2.0;
		calc_median = calc_mid_spec;
	}
	else if(list.size() == 1)
	{
		calc_mid_spec = list[0];
		calc_median = calc_mid_spec;
	}

	return calc_median;
}

template<class T>
double Median(std::vector< std::vector< T > > list,int num = 0)
{
	int calc_mid = (list[num].size() / 2) - 1, calc_mid_quarter = (list[num].size() / 4) - 1;
	int calc_mid_real = (list[num].size() / 2), calc_mid_quarter_real = (list[num].size() / 4);
	double calc_median, calc_mid_even, calc_mid_odd, calc_mid_spec;
	bool num_test = isEven(list[num].size());

	if(list[num].size() >= 4)
	{
		if(num_test == true)
		{
			calc_mid_even = (list[num][calc_mid + 1] + list[num][calc_mid]) / 2.0;
			calc_median = calc_mid_even;
		}
		else
		{
			calc_mid_odd = list[num][calc_mid_real];
			calc_median = calc_mid_odd;
		}
	}
	else if(list[num].size() == 3)
	{
		calc_mid_spec = calc_mid;
		calc_median = calc_mid_spec;
	}
	else if(list[num].size() == 2)
	{
		calc_mid_spec = (list[num][0] + list[num][1]) / 2.0;
		calc_median = calc_mid_spec;
	}
	else if(list[num].size() == 1)
	{
		calc_mid_spec = list[num][0];
		calc_median = calc_mid_spec;
	}

	return calc_median;
}

// Upper Quartile

template<class T>
double UpperQuartile(T * list,int size)
{
	int calc_mid = (size / 2) - 1, calc_mid_quarter = (size / 4) - 1;
	int calc_mid_real = (size / 2), calc_mid_quarter_real = (size / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(size);
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((size - 1) / 2);
		
	if(size >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[(calc_mid + calc_mid_quarter) + 1] + list[(calc_mid + calc_mid_quarter) + 2]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid + (calc_mid_quarter + 2)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid + (calc_mid_quarter_real + 1)] + list[calc_mid + (calc_mid_quarter_real + 2)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid + (calc_mid_quarter_real + 2)];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(size == 3)
	{
		calc_spec_quartile = (list[1] + list[2]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(size == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double UpperQuartile(std::vector< T > list)
{
	int calc_mid = (list.size() / 2) - 1, calc_mid_quarter = (list.size() / 4) - 1;
	int calc_mid_real = (list.size() / 2), calc_mid_quarter_real = (list.size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list.size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list.size() - 1) / 2);
		
	if(list.size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[(calc_mid + calc_mid_quarter) + 1] + list[(calc_mid + calc_mid_quarter) + 2]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[calc_mid + (calc_mid_quarter + 2)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[calc_mid + (calc_mid_quarter_real + 1)] + list[calc_mid + (calc_mid_quarter_real + 2)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[calc_mid + (calc_mid_quarter_real + 2)];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list.size() == 3)
	{
		calc_spec_quartile = (list[1] + list[2]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list.size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
		
	return calc_quartile;
}

template<class T>
double UpperQuartile(std::vector< std::vector< T > > list,int num = 0)
{
	int calc_mid = (list[num].size() / 2) - 1, calc_mid_quarter = (list[num].size() / 4) - 1;
	int calc_mid_real = (list[num].size() / 2), calc_mid_quarter_real = (list[num].size() / 4);
	double calc_quartile, calc_even_quartile, calc_odd_quartile, calc_spec_quartile;
	bool num_test = isEven(list[num].size());
	bool calc_test_even = isEven(calc_mid_real), calc_test_odd = isEven((list[num].size() - 1) / 2);
	
	if(list[num].size() >= 4)
	{
		if(num_test == true)
		{
			if(calc_test_even == true)
			{
				calc_even_quartile = (list[num][(calc_mid + calc_mid_quarter) + 1] + list[num][(calc_mid + calc_mid_quarter) + 2]) / 2.0;
				calc_quartile = calc_even_quartile;
			}
			else
			{
				calc_even_quartile = list[num][calc_mid + (calc_mid_quarter + 2)];
				calc_quartile = calc_even_quartile;
			}
		}
		else
		{
			if(calc_test_odd == true)
			{
				calc_odd_quartile = (list[num][calc_mid + (calc_mid_quarter_real + 1)] + list[num][calc_mid + (calc_mid_quarter_real + 2)]) / 2.0;
				calc_quartile = calc_odd_quartile;
			}
			else
			{
				calc_odd_quartile = list[num][calc_mid + (calc_mid_quarter_real + 2)];
				calc_quartile = calc_odd_quartile;
			}
		}
	}
	else if(list[num].size() == 3)
	{
		calc_spec_quartile = (list[num][1] + list[num][2]) / 2.0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 2)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	else if(list[num].size() == 1)
	{
		calc_spec_quartile = 0;
		calc_quartile = calc_spec_quartile;
	}
	
	return calc_quartile;
}

// Interquartile Range

template<class T>
double QuartileRange(T * list,int size)
{
	double calc_range, calc_quartile_lower, calc_quartile_upper;

	calc_quartile_lower = LowerQuartile(list,size);
	calc_quartile_upper = UpperQuartile(list,size);

	calc_range = calc_quartile_upper - calc_quartile_lower;

	return calc_range;
}

template<class T>
double QuartileRange(std::vector< T > list)
{
	double calc_range, calc_quartile_lower, calc_quartile_upper;

	calc_quartile_lower = LowerQuartile(list);
	calc_quartile_upper = UpperQuartile(list);

	calc_range = calc_quartile_upper - calc_quartile_lower;

	return calc_range;
}

template<class T>
double QuartileRange(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_range, calc_quartile_lower, calc_quartile_upper;

	calc_quartile_lower = LowerQuartile(list,num);
	calc_quartile_upper = UpperQuartile(list,num);

	calc_range = calc_quartile_upper - calc_quartile_lower;

	return calc_range;
}

// Minimum

template<class T>
double Min(T * list,int size)
{
	double calc_min, calc_min_temp = list[0];

	for(int count = 0; count < size; count++)
	{
		if(list[count] < calc_min_temp)
		{
			calc_min_temp = list[count];
		}
	}

	calc_min = calc_min_temp;

	return calc_min;
}

template<class T>
double Min(std::vector< T > list)
{
	double calc_min, calc_min_temp = list[0];

	for(unsigned int count = 0; count < list.size(); count++)
	{
		if(list[count] < calc_min_temp)
		{
			calc_min_temp = list[count];
		}
	}

	calc_min = calc_min_temp;

	return calc_min;
}

template<class T>
double Min(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_min, calc_min_temp = list[num][0];

	for(unsigned int count = 0; count < list[num].size(); count++)
	{
		if(list[num][count] < calc_min_temp)
		{
			calc_min_temp = list[num][count];
		}
	}

	calc_min = calc_min_temp;

	return calc_min;
}

// Maximum

template<class T>
double Max(T * list,int size)
{
	double calc_max, calc_max_temp = list[0];

	for(int count = 0; count < size; count++)
	{
		if(list[count] > calc_max_temp)
		{
			calc_max_temp = list[count];
		}
	}

	calc_max = calc_max_temp;

	return calc_max;
}

template<class T>
double Max(std::vector< T > list)
{
	double calc_max, calc_max_temp = list[0];

	for(unsigned int count = 0; count < list.size(); count++)
	{
		if(list[count] > calc_max_temp)
		{
			calc_max_temp = list[count];
		}
	}

	calc_max = calc_max_temp;

	return calc_max;
}

template<class T>
double Max(std::vector< std::vector< T > > list,int num = 0)
{
	double calc_max, calc_max_temp = list[num][0];

	for(unsigned int count = 0; count < list[num].size(); count++)
	{
		if(list[num][count] > calc_max_temp)
		{
			calc_max_temp = list[num][count];
		}
	}

	calc_max = calc_max_temp;

	return calc_max;
}