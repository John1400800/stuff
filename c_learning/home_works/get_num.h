int getline(char *s, int lim);
int isfloat(char *s);
int isint(char *s);
double atof_(char *s);
int atoi_(char *s);

#ifndef _INC_MATH
#define atof(ps) (atof_(ps))
#define atoi(ps) (atoi_(ps))
#endif
