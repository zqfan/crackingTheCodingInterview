/* 9.5
   Given a sorted array of strings which is interspersed with empty
   strings, write a method to find the location of a given string.
   Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”,
   “”, “”, “dad”, “”, “”] will return 4
   Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”,
   “”, “”, “dad”, “”, “”] will return -1 */
/* it is easy to implement this in python. but i still write with c.
   a = [“at”, “”, “”, “”, “ball”, “”, “”, “car”,
   “”, “”, “dad”, “”, “”]
   a.index("ball") */

#include <stdio.h>
#include <string.h>

int get_index(const char arr[][20], int start, int end,
              const char * target)
{
  if ( start > end )
    return -1;
  if ( start == end )
    return strcmp(arr[start], target) == 0 ? start : -1;
  int m = ( start + end ) / 2;
  while ( arr[m][0] == '\0' ) {
    m--;
    if ( m < start )
      return get_index(arr, ((start + end) / 2) + 1, end, target);
  }
  int r = strcmp(arr[m], target);
  if ( r == 0 )
    return m;
  else if ( r > 0 )
    return get_index(arr, start, m - 1, target);
  m = ( start + end ) / 2 + 1;
  while ( arr[m][0] == '\0' ) {
    m++;
    if ( m > end )
      return -1;
  }
  return get_index(arr, m, end, target);
}

int main(int argc, char * argv[])
{
  char a[][20] = {"at", "", "", "", "ball", "", "", "car",
                  "", "", "dad", "", ""};
  printf("%d\n", get_index(a, 0, 12, "ball"));
  return 0;
}
