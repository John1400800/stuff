#include <stdio.h>
#include "get_num.h"

#define MAXLINE 100

#define M_PI 3.14159265358979323846
#define max(a, b) ((a) > (b) ? (a) : (b)) 
#define min(a, b) ((a) < (b) ? (a) : (b)) 
#define ring_area(r1, r2) (M_PI*max((r1), (r2))*max((r1), (r2)) - M_PI*min((r1), (r2))*min((r1), (r2)))

int main(void) {
	char buffs[MAXLINE+1];
	int i;
	double r1, r2, curr_area, max_area;
	i = 3;
	max_area = 0;
	while (i--) {
		printf("введите внешний радиус: ");
		getline(buffs, MAXLINE);
		while (!isfloat(buffs)) {
	        printf("некоректный ввод, введите еще раз: ");
	        getline(buffs, MAXLINE);
		}
		r1 = atof(buffs);
		printf("введите внутренний радиус: ");
		getline(buffs, MAXLINE);
		while (!isfloat(buffs)) {
	        printf("некоректный ввод, введите еще раз: ");
	        getline(buffs, MAXLINE);
		}
		r2 = atof(buffs);
		if ((curr_area = ring_area(r1, r2)) > max_area)
			max_area = curr_area;
	}
	printf("%f", max_area);
	return 0;
}
