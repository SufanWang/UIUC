//
//  main.cpp
//  Stable Marriage Problem
//
//  Created by Ramavarapu Sreenivas on 8/29/14.
//  Copyright (c) 2014 Ramavarapu Sreenivas. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class stable_marriage_instance
{
    // Private
    int no_of_couples;
    vector <vector <int> > Preference_of_men;
    vector <vector <int> > Preference_of_women;
    vector <int> match_for_men;
    vector <int> match_for_women;

    // private member function: checks if anybody is free in boolean "my_array"
    // returns the index of the first-person who is free in "my_array"
    // if no one is free it returns a -1.
    int anybody_free(vector <bool> my_array)
    {
        // fill the necessary code for this function
   
        for (int i = 0; i < my_array.size(); i++) {
            if (my_array[i] == true) {
                return i;
            }
        }
        return -1;
    }

    // private member function: if index1 is ranked higher than index2
    // in a preference array called "my_array" it returns "true"; otherwise
    // it returns "false"
    bool rank_check(vector <int> my_array, int index1, int index2)
    {
        // fill the necessary code for this function
        //bool result = true;
        for (int i = 0; i < my_array.size(); i++) {
            if (my_array[i] ==index1) {
                return true;
                //result = true;
                //break;
            }
            if (my_array[i] == index2) {
                return false;
                //result = false;
                //break;
            }
        }
       // return(result);
    }

    // private member function: implements the Gale-Shapley algorithm
    void Gale_Shapley()
    {
        vector <bool> is_man_free;
        vector <bool> is_woman_free;
        vector <vector <bool> > has_this_man_proposed_to_this_woman;

        int man_index, woman_index;

        // initializing everything
        vector<bool>temp1;
        for (int i = 0; i < no_of_couples; i++) {
            temp1.push_back(false);
        }
        for (int i = 0; i < no_of_couples; i++)
        {
            // do the necessary initialization here
            is_man_free.push_back(true);
            is_woman_free.push_back(true);
            match_for_men.push_back(-1);
            match_for_women.push_back(-1);
            has_this_man_proposed_to_this_woman.push_back(temp1);


        }

        // Gale-Shapley Algorithm
        while ((man_index = anybody_free(is_man_free)) >= 0)
        {
            // fill the necessary code here

            for (int i = 0; i < no_of_couples; i++) {
                if (has_this_man_proposed_to_this_woman[man_index][Preference_of_men[man_index][i]] == false) {
                    woman_index = Preference_of_men[man_index][i];
                    break;
                }
            }
            if (is_woman_free[woman_index] == true) {
                match_for_men[man_index] = woman_index;
                match_for_women[woman_index] = man_index;
                is_man_free[man_index] = false;
                is_woman_free[woman_index] = false;
                has_this_man_proposed_to_this_woman[man_index][woman_index] = true;
            }
            else {
                if (rank_check(Preference_of_women[woman_index], man_index, match_for_women[woman_index]) == true) {
                    is_man_free[man_index] = false;
                    is_man_free[match_for_women[woman_index]] = true;
      
                    match_for_women[woman_index] = man_index;
                    match_for_men[man_index] = woman_index;
                    has_this_man_proposed_to_this_woman[man_index][woman_index] = true;
                }
                else {
                    has_this_man_proposed_to_this_woman[man_index][woman_index] = true;
                }
            }

        }
    }

    // private member function: reads data
    void read_data(int argc, const char* argv[])
    {
        // fill the necessary code here.  The first entry in the input
        // file is the #couples, followed by the preferences of the men
        // and preferences of the women.  Keep in mind all indices start
        // from 0.
        ifstream input_filename(argv[1]);
        if (input_filename.is_open()) {
            cout << "Input File Name: " << argv[1] << endl;

            int value_just_read;
            vector <int> inputfile;
            input_filename >> value_just_read;
            no_of_couples = value_just_read;
            cout << "Number of couple= " << value_just_read << endl;
            cout << endl;
            cout << "Preferrences of men " << endl;
            cout << "-----------------------------" << endl;
           
            for (int i = 0; i < no_of_couples; i++) {
                cout << endl << "(" << i << "):";
                for (int j = 0; j < no_of_couples; j++) {
                    input_filename >> value_just_read;
                    inputfile.push_back(value_just_read);
                    cout << value_just_read << " ";
                }
            }
            cout << endl;
            cout <<endl<< "Preferrences of women " << endl;
            cout << "-----------------------------" << endl;
            for (int i = 0; i < no_of_couples; i++) {
                cout << endl << "(" << i << "):";
                for (int j = 0; j < no_of_couples; j++) {
                    input_filename >> value_just_read;
                    inputfile.push_back(value_just_read);
                    cout << value_just_read << " ";
                }
            }
            vector <int>temp;
            for (int i = 0; i < no_of_couples; i++) {
                for (int j = 0; j < no_of_couples; j++) {
                    temp.push_back(inputfile[i * no_of_couples + j]);
                }
                Preference_of_men.push_back(temp);
                temp.clear();
            }
            for (int i = 0; i < no_of_couples; i++) {
                for (int j = 0; j < no_of_couples; j++) {
                    temp.push_back(inputfile[no_of_couples * no_of_couples + i * no_of_couples + j]);
                }
                Preference_of_women.push_back(temp);
                temp.clear();
            }

        }
        else {
            cout << "Input file missing" << endl;
            exit(0);
        }
    }

    // private member function: print solution
    void print_soln()
    {
        // write the appropriate code here
        cout << endl;
        cout << endl<< "Matching for men" << endl;
        for (int i = 0; i < no_of_couples; i++) {
            cout << "Man: " << i << " -> " << "Woman: " << match_for_men[i] << endl;
        }
        cout <<endl<< "Matching for women" << endl;
        for (int i = 0; i < no_of_couples; i++) {
            cout << "Woman: " << i << " -> " << "Man: " << match_for_women[i] << endl;
        }
    }

public:
    void solve_it(int argc, const char* argv[])
    {
        read_data(argc, argv);

        Gale_Shapley();

        print_soln();
    }
};

int main(int argc, const char* argv[])
{
    stable_marriage_instance x;
    x.solve_it(argc, argv);
}
