/* 9.3
   Given a sorted array of n integers that has been rotated an unknown
   number of times, give an O(log n) algorithm that finds an element
   in the array. You may assume that the array was originally sorted
   in increasing order.
   EXAMPLE:
   Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
   Output: 8 (the index of 5 in the array) */
#include <stdio.h>

/* get target index from array in increasing order.
   if the target is duplicated, then return the first one.
   :param end is a valid element of arr. */
int binary_search(const int * arr, int start, int end, int target)
{
  if ( start == end )
    return target == arr[start] ? start: -1;
  int m = ( start + end ) / 2;
  if ( target <= arr[m] )
    return binary_search(arr, start, m, target);
  else
    return binary_search(arr, m+1, end, target);
}

/* search target in arr[start,end], the arr is a rotated increasing
   array, and the arr[end] is valid element.
   if target is duplicated, return the first one. */
int get_index(const int * arr, int start, int end, int target)
{
  if ( arr[start] <= arr[end] )
    return binary_search(arr, start, end, target);
  int m = ( start + end ) / 2;
  if ( arr[start] <= arr[m] ) { // left is in order
    if ( arr[start] <= target && target <= arr[m] ) // target in left
      return binary_search(arr, start, m, target);
    else // target may be in right side
      return get_index(arr, m+1, end, target);
  } else { // right is in order
    if ( arr[m] < target && target <= arr[end] ) // target in right
      return binary_search(arr, m+1, end, target);
    else // target may be in left side
      return get_index(arr, start, m, target);
  }
}

int main(int argc, char * argv[])
{
  int a[] = {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14};
  printf("%d\n",get_index(a, 0, 11, 5));
  return 0;
}
