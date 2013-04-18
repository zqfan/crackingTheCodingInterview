/* Write code to remove duplicates from an unsorted linked list.
   FOLLOW UP
   How would you solve this problem if a temporary buffer is not
   allowed?
*/
#include <stdio.h>
#include "link.h"

/* O(n*n), stupid method */
int remove_dup(s_node* root)
{
  s_node* i = root;
  s_node* j;
  s_node* k;
  while ( i ) {
    j = i->next;
    while ( j ) {
      if ( i->data == j->data ) {
        k = j->next;
        delete_node(root, j);
        j = k;
        continue;
      }
      j = j->next;
    }
    i = i->next;
  }
  return 0;
}

int main(int argc, char* argv[])
{
  int arr[10] = {1,2,3,3,1,1,3,3,5,6};
  s_node* root = create_linked_list(arr,10);
  remove_dup(root);
  print_linked_list(root);
  clear_linked_list(root);
  return 0;
}
