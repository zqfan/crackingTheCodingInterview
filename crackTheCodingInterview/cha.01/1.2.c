/* Write code to reverse a C-Style String. (C-String means that “abcd”
 * is represented as five characters, including the null character.)
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* reverse source to dest, return the length of source */
int reverse(char* source, char* dest)
{
  int len = strlen(source);
  int i;
  for ( i = 0; i < len; i++) {
    dest[len-i-1] = source[i];
  }
  dest[len] = '\0';
  return len;
}

int main(int argc, char* argv[])
{
  if (argc < 2) {
    return 0;
  }
  char* dest = malloc(sizeof(char)*(strlen(argv[1])+1));
  reverse(argv[1],dest);
  printf("%s\n",dest);
  free(dest);
  return 0;
}
