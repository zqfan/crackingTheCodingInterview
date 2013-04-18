/* Write a program to swap odd and even bits in an integer with as few
   instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2
   and bit 3 are swapped, etc).

   00011011
   00100111

   ((n & 01) << 1) | ((n & 10) >> 1)
*/
#include <stdio.h>

int swap_bit(int n)
{
  int m = 0;
  int i = 0;
  while (n != 0) {
    switch ( n & 3 ) {
    case 0: break;
    case 1: m += (1 << (i+1)); break;
    case 2: m += (1 << i); break;
    case 3: m += (3 << i); break;
    default:return -1;
    }
    n = n >> 2;
    i += 2;
  }
  return m;
}

int main(int argc, char *argv[])
{
  printf("%d\n",swap_bit(27));
  return 0;
}
