/* An array A[1...n] contains all the integers from 0 to n except for
   one number which is missing. In this problem, we cannot access an
   entire integer in A with a single operation. The elements of A are
   represented in binary, and the only operation we can use to access
   them is “fetch the jth bit of A[i]”, which takes constant time.
   Write code to find the missing integer. Can you do it in O(n) time?

   Analyse:
   n = 4, miss = 2
   000, 001, 011, 100,
   sum = 8 but should be 10
   so we caculate the sum and the det of the expected sum is the
   missing. further more, the jth bit of A[i] is a value of
   a[i][j] << j, so the sum should be evaled by all bits of A[]
   because all data is non-negative.
*/
#include <stdio.h>

// i don't know how to fetch jth bit from a array
// in fact, the int *a should be a byte array
int find_miss(int *a, int len)
{
  int i, j, k, sum=0;
  for ( i = 0; i < len; i++ ) {
    k = 0;
    for ( j = 0; j < 32; j++ ) {
      sum += (a[i][j] << j);
    }
  }
  return ((len + 1)*len)/2 - sum;
}

int main(int argc, char *argv[])
{
  int a[] = {0,1,3,4};
  printf("%d\n",find_miss(a, sizeof(a)));
  return 0;
}
