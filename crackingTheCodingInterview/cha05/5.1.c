#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* 5.1:
   You are given two 32-bit numbers, N and M, and two bit positions, i
   and j. Write a method to set all bits between i and j in N equal to
   M (e.g., M becomes a substring of N located at i and starting at j).
   EXAMPLE:
   Input: N = 10000000000, M = 10101, i = 2, j = 6
   Output: N = 10001010100
*/
// TODO(fan): find a 32-bit type instead of int
int replace(int n, int m, int i, int j)
{
  if ( 32 < j or j < i or i < 0 )
    return n;
  int t = 1;
  for ( int x = i; x <= j; x++)
    t = (t << 1) + 1;
  t <<= i;
  m = (m << i) | (~t);
  return (n | t) & m;
}

int main(int argc, char *argv[])
{
  r = replace(1024,21,2,6);
  printf("%d\n",r);
  return 0;
}
