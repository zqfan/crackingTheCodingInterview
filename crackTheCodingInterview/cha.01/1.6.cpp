/* Given an image represented by an NxN matrix, where each pixel in
   the image is 4 bytes, write a method to rotate the image by 90
   degrees. Can you do this in place?

   Analyze:
*/
#include <iostream>
using namespace std;

typedef struct _pixel
{
  char red;
  char green;
  char blue;
  char alpha;
} s_pixel;

void _get_next(int width, int height, int * i, int * j, int degree)
{
  int tmp = 0;
  switch ( degree ) {
  case 90:
    tmp = *i;
    *i = *j;
    *j = width - tmp - 1;
    break;
  case 180:
    *i = width - *i - 1;
    *j = height - *j - 1;
    break;
  case 270:
    tmp = *i;
    *i = height - *j - 1;
    *j = tmp;
    break;
  default:return;
  }
}

int rotate_image(s_pixel ** image, int width, int height, int degree)
{
  // find the relation
  // for each image[i][j]
  int next_i = 0, next_j = 0;
  s_pixel source, target;
  for ( int i = 0; i < width; i++ ) {
    for ( int j = i; j < height - i - 1; j++ ) {
      next_i = i;
      next_j = j;
      // shift the 4 point
      for ( int k = 0; k < 4; k++ ) {
        if ( i == next_i && j == next_j )
          source = image[i][j];
        else
          source = target;
        _get_next(width, height, &next_i, &next_j, degree);
        target = image[next_i][next_j];
        image[next_i][next_j] = source;
      } // end k
    } // end j
  } // end i
  return 0;
}

int main()
{
  s_pixel ** a = new s_pixel *[2];
  a[0] = new s_pixel[2];
  s_pixel p = {'0','0','0','0'};
  a[0][0] = p;
  p.red = '1';
  a[0][1] = p;
  a[1] = new s_pixel[2];
  p.red = '2';
  a[1][0] = p;
  p.red = '3';
  a[1][1] = p;
  rotate_image(a,2,2,90);
  cout << a[0][0].red << a[0][1].red
       << a[1][0].red << a[1][1].red << endl;
  delete [] a[0];
  delete [] a[1];
  delete [] a;
  return 0;
}
