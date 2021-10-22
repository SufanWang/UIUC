/*
 *  sudoku.h
 *  Sudoku
 *  Created by Prof. Ramavarapu Sreenivas
 *  Inspired by: http://web.eecs.utk.edu/courses/spring2012/cs140/Notes/Sudoku/index.html
*/

#ifndef sudoku
#define sudoku
#include <iostream>
#include <vector>
#include <fstream>
using std::vector;
using namespace std;
class Sudoku
{
	// Private
	int puzzle[9][9];

	// Private member function that checks if the named row is valid
	bool row_valid(int row, int s)
	{
		// write code that checks if "row" is valid
		for (int i = 0; i < 9; i++) {
			if (puzzle[row][i] == s) return false;
		}
		return true;
	}

	// Private member function that checks if the named column is valid
	bool col_valid(int col, int s)
	{
		// check validity of "col" 
		for (int i = 0; i < 9; i++) {
			if (puzzle[i][col] == s) return false;
		}
		return true;

	}

	// Private member function that checks if the named 3x3 block is valid
	bool block_valid(int row, int col, int s)
	{
		// check 3 x 3 block validity 
		for (int i = row / 3 * 3; i < row / 3 * 3 + 3; i++) {
			for (int j = col / 3 * 3; j < col / 3 * 3 + 3; j++)
				if (puzzle[i][j] == s)
					return false;
		}
		return true;
	}
	

public:
	// Public member function that reads the incomplete puzzle
	// we are not doing any checks on the input puzzle -- that is,
	// we are assuming they are indeed valid
	void read_puzzle(int argc, char* const argv[])
	{
		// write code that reads the input puzzle using the 
		// guidelines of figure 23 of the bootcamp material
		//I put the input files in the folser Debug and set the command parameter input3
		//when need to change the input file,just change the parameter
		ifstream input_file(argv[1]);
		if (input_file.is_open()) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					input_file >> puzzle[i][j];
				}
			}
			input_file.close();
		}
		else cout << "Input file " << argv[1] << " does not exist in PWD" << endl;
	}

	// Public member function that prints the puzzle when called
	void print_puzzle()
	{
		std::cout << std::endl << "Board Position" << std::endl;
		for (int i = 0; i < 9; i++)
		{
			for (int j = 0; j < 9; j++)
			{
				// check if we have a legitimate integer between 1 and 9
				if ((puzzle[i][j] >= 1) && (puzzle[i][j] <= 9))
				{
					// printing initial value of the puzzle with some formatting
					std::cout << puzzle[i][j] << " ";
				}
				else {
					// printing initial value of the puzzle with some formatting
					std::cout << "X ";
				}
			}
			std::cout << std::endl;
		}
	}
	// Private member function that checks if all the constraints are satisfied
	bool check(int row, int col, int s)
	{
		if (row_valid(row, s) && col_valid(col, s) && block_valid(row, col, s)) {
			return true;
		}
		else 
			return false;
	}
	bool empty(int&row, int&col)
	{
		for (row = 0; row < 9; row++) {
			for (col = 0; col < 9; col++) {
				if (puzzle[row][col] == 0) return true;
			}
		}
		return false;
	}

	// Public member function that (recursively) implements the brute-force 
	// search for possible solutions to the incomplete Sudoku puzzle
	bool Solve(int row, int col)
	{
		// this part of the code identifies the row and col number of the 
		// first incomplete (i.e. 0) entry in the puzzle.  If the puzzle has
		// no zeros, the variable row will be 9 => the puzzle is done, as 
		// each entry is row-, col- and block-valid...

		// use the pseudo code of figure 3 of the description
		if (empty(row, col)==true) {
			for (int s = 1; s < 10; s++) {
				if (check(row, col, s) == true) {
					puzzle[row][col] = s;
					if (Solve(row, col) == true)
					{
						return true;
					}
				}
				puzzle[row][col] = 0;
			}
			return false;
		}
		else return true;
	};
	public:

		int n = 0;
		bool alternate_Solve(int row, int col)
		{
			if (empty(row, col)==true) {
				for (int s = 1; s < 10; s++) {
					if (check(row, col, s)==true){
						puzzle[row][col] = s;
						if (alternate_Solve(row, col)==true) {
							n++;
							std::cout << std::endl;
							cout << "Solution # " << n << ":" << endl;
							print_puzzle();
						}
					}
				puzzle[row][col] = 0;
				}
				return false;
			}
			else return true;
		};
};

#endif