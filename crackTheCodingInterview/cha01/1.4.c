/* Write a method to decide if two strings are anagrams or not.
   Analyse:
   * length of two strings must be same;
   * statistics of all character should be same;
   * is there any character not in [a-zA-Z]?
   * is there any non-english character? */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* only accept ANSCII string, if s1 and s2 are anagrams then return 0,
   else return 1.
   cost: O(N1+N2) */
int is_anagram(const char* s1, const char* s2)
{
  int len1 = strlen(s1);
  int len2 = strlen(s2);
  if ( len1 != len2 )
    return 1;
  int statistics[128] = {0};
  int i;
  for ( i = 0; i < len1; i++ )
    statistics[s1[i]]++;
  for ( i = 0; i < len2; i++ )
    statistics[s2[i]]--;
  for ( i = 0; i < 128; i++ )
    if (statistics[i] != 0 )
      return 1;
  return 0;
}

int main(int argc, char* argv[])
{
  if ( argc < 3 )
    return 1;
  int r = is_anagram(argv[1], argv[2]);
  printf("%d\n",r);
  return 0;
}
