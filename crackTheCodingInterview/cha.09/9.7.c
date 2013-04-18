/* 9.7
   A circus is designing a tower routine consisting of people standing
   atop one another’s shoulders. For practical and aesthetic reasons,
   each person must be both shorter and lighter than the person below
   him or her. Given the heights and weights of each person in the
   circus, write a method to compute the largest possible number of
   people in such a tower.
   EXAMPLE:
   Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95)
   (68, 110)
   Output: The longest tower is length 6 and includes from top to
   bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190) */
#include <stdlib.h>
#include <stdio.h>
#include <memory.h>

typedef struct _element
{
  int height;
  int weight;
} s_element;

int compare(const void * a, const void * b)
{
  s_element * pa = (s_element *)a;
  s_element * pb = (s_element *)b;
  if ( pa->height == pb->height ) {
    if ( pa->weight == pb->weight )
      return 0;
    else if ( pa->weight < pb->weight )
      return -1;
    else
      return 1;
  } else if ( pa->height < pb->height )
    return -1;
  else
    return 1;
}

int max_tower(s_element * parr, int len)
{
  qsort(parr, len, sizeof(s_element), compare);
  int * pmax = (int *)malloc(len*sizeof(int));
  memset(pmax, 0, len*sizeof(int));
  pmax[0] = 1;
  int i, j;
  for ( i = 1; i < len; i++ ) {
    for ( j = 0; j < i; j++ ) {
      if ( parr[i].weight >= parr[j].weight
           && pmax[i] < pmax[j] + 1 )
        pmax[i] = pmax[j] + 1;
    }
  }
  int max = 0;
  for ( i = 0; i < len; i++ ) {
    if ( max < pmax[i] )
      max = pmax[i];
  }
  return max;
}

int main(int argc, char * argv[])
{
  s_element arr[] = {{65,100},{70,150},{56,90},{75,90},{60,95},
                     {68,110}};
  printf("%d\n",max_tower(arr, sizeof(arr)/sizeof(arr[0])));
  return 0;
}
