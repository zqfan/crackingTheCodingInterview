/* Write an algorithm such that if an element in an MxN matrix is 0,
   its entire row and column is set to 0.
   Analyse:
   two array store the row and column should be set to 0
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int process(int** matrix, int row, int col)
{
  int * row_flag = malloc(sizeof(int)*row);
  int * col_flag = malloc(sizeof(int)*col);
  int i,j;
  memset(row_flag, '\0', sizeof(int)*row);
  memset(col_flag, '\0', sizeof(int)*col);
  for ( i = 0; i < row; i++ ) {
    for ( j = 0; j < col; j++ ) {
      if ( *((int*)matrix + col*i + j) == 0 ) {
        row_flag[i] = 1;
        col_flag[j] = 1;
      }
    }
  }
  for ( i = 0; i < row; i++ ) {
    if ( row_flag[i] == 1 ) {
      for ( j = 0; j < col; j++ )
        *((int*)matrix + col*i + j) = 0;
    }
  }
  for ( i = 0; i < col; i++ ) {
    if ( col_flag[i] == 1 ) {
      for ( j = 0; j < row; j++ )
        *((int*)matrix + col*j + i) = 0;
    }
  }
  free(row_flag);
  free(col_flag);
  return 0;
}

int main(int argc, char* argv[])
{
  int i,j;
  int matrix[3][3] = {{1,1,1},{1,0,1},{1,1,1}};
  process((int**)matrix, 3, 3);
  for ( i = 0; i < 3; i++ ) {
    for ( j = 0; j < 3; j++ ) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }
  return 0;
}

