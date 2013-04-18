/* Write a method to replace all spaces in a string with ‘%20’.
   Analyse:
   * the point is that strlen(" ") is not equal to strlen("%20");
   * is space include [\n\t]? i think it don't because \n\t can be
   replace by other string. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* replace pattern with dest_pattern, return the new string.
   you must free() the return pointer. */
char* replace(const char* source, const char pattern,
            const char* dest_pattern)
{
  int len = strlen(source);
  int i, j, k, count = 0;
  int dest_pattern_len = strlen(dest_pattern);
  for ( i = 0; i < len; i++ )
    if ( source[i] == pattern )
      count++;
  int dest_len = len + count * (strlen(dest_pattern) - 1) + 1;
  char* dest = malloc(sizeof(char) * dest_len);
  for ( i = 0, j = 0; i < len; i++, j++ ) {
    if ( source[i] == pattern ) {
      for ( k = 0; k < dest_pattern_len; k++, j++ )
        dest[j] = dest_pattern[k];
      j--;
    } else
      dest[j] = source[i];
  }
  return dest;
}

int main(int argc, char* argv[])
{
  if ( argc < 2 )
    return 1;
  char* dest = replace(argv[1], ' ', "%20");
  printf("%s\n", dest);
  free(dest);
  return 0;
}
