/* 9.1
   You are given two sorted arrays, A and B, and A has a large enough
   buffer at the end to hold B. Write a method to merge B into A in
   sorted order.
*/
#include <stdio.h>

/* 1. len_t is the element count of target's, so does len_s to source.
   2. the buffer of target should can hold all elements of target and
   source.
   3. target and source has already been sorted in asce order.
*/
void merge_by_sort(int * target, int len_t,
                   const int * source, int len_s)
{
  int t = len_t - 1;
  int s = len_s - 1;
  for ( int i = t + s + 1; i >= 0; i-- ) {
    if ( target[t] > source[s] )
      target[i] = target[t--];
    else
      target[i] = source[s--];
  }
}

int main(int argc, char * argv[])
{
  int a[10] = {1,3,5,7};
  int b[] = {2,4,6,8};
  merge_by_sort(a, 4, b, 4);
  for ( int i = 0; i < 8; i++ )
    printf("%d ", a[i]);
  return 0;
}
