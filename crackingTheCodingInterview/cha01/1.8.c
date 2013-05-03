/* Assume you have a method isSubstring which checks if one word is a
   substring of another. Given two strings, s1 and s2, write code to
   check if s2 is a rotation of s1 using only one call to isSubstring
   (i.e., “waterbottle” is a rotation of “erbottlewat”).
   Analyse:
   just concat a string to itself and you can use isSubstring()
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int isSubstring(const char* source, const char* pattern)
{
  char* str = strstr(source, pattern);
  if ( str == NULL )
    return 1;
  else
    return 0;
}

int main(int argc, char* argv[])
{
  if ( argc < 3 )
    return 1;
  int len = strlen(argv[1]) * 2 + 1;
  char* dest = malloc(sizeof(char) * len);
  memset(dest, '\0', len * sizeof(char));
  strcat(dest, argv[1]);
  strcat(dest, argv[1]);
  int r = isSubstring(dest, argv[2]);
  printf("%d\n", r);
  free(dest);
  return 0;
}