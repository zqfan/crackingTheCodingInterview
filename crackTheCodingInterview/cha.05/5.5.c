/* Write a function to determine the number of bits required to
   convert integer A to integer B.
   Input: 31, 14
   Output: 2
*/
#include <stdio.h>

int bit_count(int a, int b)
{
  int count = 0;
  int c = 0;
  for ( c = a ^ b; c != 0; c >>= 1 )
    count += c & 1;
  return c;
}
