/* Implement an algorithm to delete a node in the middle of a single
   linked list, given only access to that node.
   EXAMPLE
   Input: the node ‘c’ from the linked list a->b->c->d->e
   Result: nothing is returned, but the new linked list looks like
   a->b->d->e

   Analyse:
   since i just can access the c node, the only way i can do it is
   copy d to c and free d.
*/
#include <stdlib.h>
#include "link.h"

int remove_middle_node(s_node* node)
{
  if ( NULL == node || NULL == node->next )
    return -1;
  s_node* next = node->next;
  node->data = next->data;
  node->next = next->next;
  free(next);
  return 0;
}

int main(int argc, char* argv[])
{
  int a[] = {1,2,3,4,5};
  s_node* root = create_linked_list(a, sizeof(a)/sizeof(a[0]));
  remove_middle_node(root->next);
  print_linked_list(root);
  clear_linked_list(root);
  return 0;
}
