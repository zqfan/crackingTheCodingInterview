/* Design an algorithm and write code to remove the duplicate
   characters in a string without using any additional buffer. NOTE:
   One or two additional variables are fine. An extra copy of the
   array is not.
   FOLLOW UP
   Write the test cases for this method.*/

/* Analyze:
   int index: there must one iterator at least;
   int index2: there can be another iterator to downgrade complexity
   int last_undup: a flag which is not necessary but will prune some
   loop. */
#include <stdio.h>
#include <string.h>

int remove_duplicate(char* source)
{
  int i,j;
  for ( i = 0; source[i] != '\0'; i++ ) {
    // loop the previous character
    for ( j = 0; j < i; j++ ) {
      // if duplicate, remove current character
      if ( source[i] == source[j] ) {
        for ( j = i; source[j] != '\0'; j++ ) {
          source[j] = source[j+1];
        }
        i--;
        break;
      } // end if
    } // end external for j
  } // end for i
}

int main(int argc, char* argv[])
{
  if (argc < 2)
    return 0;
  remove_duplicate(argv[1]);
  printf("%s\n",argv[1]);
  return 0;
}
