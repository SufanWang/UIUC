/*
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <algorithm>
using namespace std;

double up_factor, uptick_prob, risk_free_rate, strike_price, downtick_prob, notick_prob;
double initial_stock_price, expiration_time, volatility, R;
int no_of_divisions;

double american_call_option(int k, int i, double**call_m) {
	if (k == no_of_divisions) {
		return max(0.0, (initial_stock_price * pow(up_factor, i) - strike_price));
	}
	if (call_m[k][no_of_divisions + i] == -1)
	{
		call_m[k][no_of_divisions + i] =
			max((initial_stock_price * pow(up_factor, i) - strike_price),
				(uptick_prob * american_call_option(k + 1, i + 1, call_m) +
					notick_prob * american_call_option(k + 1, i, call_m) +
					downtick_prob * american_call_option(k + 1, i - 1, call_m)) / R);
		return call_m[k][no_of_divisions + i];
	}
	else
	{
		return call_m[k][no_of_divisions + i];
	}
}

double american_put_option(int k, int i, double**put_m) {
	if (k == no_of_divisions)
		return max(0.0, (strike_price - initial_stock_price * pow(up_factor, i)));
	if (put_m[k][no_of_divisions + i] == -1) {
		put_m[k][no_of_divisions + i] =
			max((strike_price - initial_stock_price * pow(up_factor, i)),
				(uptick_prob * american_put_option(k + 1, i + 1, put_m) +
					notick_prob * american_put_option(k + 1, i, put_m) +
					downtick_prob * american_put_option(k + 1, i - 1, put_m)) / R);
		return put_m[k][no_of_divisions + i];
	}
	else
	{
		return put_m[k][no_of_divisions + i];
	}
}
//part 1
int main(int argc, char* argv[])
{

	sscanf(argv[1], "%lf", &expiration_time);
	sscanf(argv[2], "%d", &no_of_divisions);
	sscanf(argv[3], "%lf", &risk_free_rate);
	sscanf(argv[4], "%lf", &volatility);
	sscanf(argv[5], "%lf", &initial_stock_price);
	sscanf(argv[6], "%lf", &strike_price);

	up_factor = exp(volatility * sqrt(2.0 * (expiration_time / ((double)no_of_divisions))));
	R = exp(risk_free_rate * expiration_time / ((double)no_of_divisions));
	uptick_prob = pow(((sqrt(R) - (1 / sqrt(up_factor))) / (sqrt(up_factor) - (1 / sqrt(up_factor)))), 2.0);
	downtick_prob = pow(((sqrt(up_factor) - sqrt(R)) / (sqrt(up_factor) - (1 / sqrt(up_factor)))), 2.0);
	notick_prob = 1 - uptick_prob - downtick_prob;

	double** call_m;
	call_m = new double* [no_of_divisions];
	for (int i = 0; i < no_of_divisions; i++)
		call_m[i] = new double[2 * no_of_divisions + 1];
	for (int i = 0; i < no_of_divisions; i++)
		for (int j = 0; j < 2 * no_of_divisions + 1; j++)
			call_m[i][j] = -1;

	double** put_m;
	put_m = new double* [no_of_divisions];
	for (int i = 0; i < no_of_divisions; i++)
		put_m[i] = new double[2 * no_of_divisions + 1];
	for (int i = 0; i < no_of_divisions; i++)
		for (int j = 0; j < 2 * no_of_divisions + 1; j++)
			put_m[i][j] = -1;

	cout << "Recursive Trinomial American-Asian Option Pricing" << endl;
	cout << "Expiration Time (Years) = " << expiration_time << endl;
	cout << "Number of Divisions = " << no_of_divisions << endl;
	cout << "Risk Free Interest Rate = " << risk_free_rate << endl;
	cout << "Volatility (%age of stock value) = " << volatility * 100 << endl;
	cout << "Initial Stock Price = " << initial_stock_price << endl;
	cout << "Strike Price = " << strike_price << endl;
	cout << "--------------------------------------" << endl;
	cout << "R = " << R << endl;
	cout << "Up Factor = " << up_factor << endl;
	cout << "Uptick Probability = " << uptick_prob << endl;
	cout << "Downtick Probability = " << downtick_prob << endl;
	cout << "Notick Probability = " << notick_prob << endl;
	cout << "--------------------------------------" << endl;
	//call price
	double call_price = american_call_option(0, 0, call_m);
	cout << "Price of an American Call Option = " << call_price << endl;
	//put price
	double put_price = american_put_option(0, 0, put_m);
	cout << "Price of an American Put Option = " << put_price << endl;

}*/