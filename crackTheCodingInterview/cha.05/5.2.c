#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
/* 5.2:
   Given a (decimal - e.g. 3.72) number that is passed in as a string,
   print the binary representation. If the number can not be
   represented accurately in binary, print “ERROR”
*/
// assume the number can be presented by 2 32-bit unit.
char * convert2binary(const char *number)
{
  char *r = (char *)malloc(sizeof(char)*66);
  int det = index(number, '.') - number;
  int i;
  char p[33];
  for ( i = 0; i < det && i < 32; i++)
    p[i] = number[i];
  p[i] = '\0';
  int integer = atoi(p);
  i = 0;
  char tmp[33];
  while ( integer > 0 && i < 32 ) {
    tmp[i++] = integer % 2 + '0';
    integer /= 2;
  }
  tmp[i] = '\0';
  int j;
  for ( i = strlen(tmp) - 1, j = 0; i >= 0; i--, j++ )
    r[j] = tmp[i];
  r[j] = '\0';
  const char *d = index(number, '.');
  if ( NULL == d )
    return r;
  r[j++] = '.';
  double decimal = atof(d);
  while ( decimal != 0 ) {
    if (j > 64) {
      return strcpy(r,"ERROR");
    }
    decimal *= 2;
    if (decimal >= 1) {
      r[j++] = '1';
      decimal -= 1;
    }
    r[j++] = '0';
  }
  r[j] = '\0';
  return r;
}

int main(int argc, char *argv[])
{
  char *r = convert2binary("3.75");
  printf("%s\n", r);
  free(r);
  return 0;
}
