/*
 *  card_game.h
 *  Card Game
 *
 *  Created by Ramavarapu Sreenivas
*/

#ifndef	CARDGAME_H
#define CARDGAME_H
#include <algorithm>
using namespace std;

double value(int r, int b, double **m)
{
	if (0 == r)
		return ((double)b);
	if (0 == b)
		return (0);
	if (m[r][b] == -1) {
		double term1 = ((double)r / (r + b)) * value(r - 1, b,m);

		double term2 = ((double)b / (r + b)) * value(r, b - 1,m);

		m[r][b] = max((term1 + term2), (double)(b - r));

	}
	return m[r][b];
}
#endif
