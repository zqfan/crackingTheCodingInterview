/* Given a circular linked list, implement an algorithm which returns
   node at the beginning of the loop.
   DEFINITION
   Circular linked list: A (corrupt) linked list in which a node’s
   next pointer points to an earlier node, so as to make a loop in the 
   linked list.
   EXAMPLE
   input: A -> B -> C -> D -> E -> C [the same C as earlier]
   output: C

   Analyze:
   get first loop, not all, not the biggest
*/
#include <stdlib.h>
#include <stdio.h>
#include "link.h"

s_node* get_first_loop_head(s_node* root)
{
  if ( NULL == root )
    return NULL;
  s_node* cur = root->next;
  s_node* index = NULL;
  int det_cur = 0; // det from root to cur
  int det_index = 0; // det from root to index
  while ( cur ) {
    if ( cur->next == cur )
      return cur;
    det_cur++;
    index = root;
    det_index = 0;
    while ( index != cur ) {
      index = index->next;
      det_index++;
    }
    if ( det_index < det_cur - 1 )
      return cur;
    cur = cur->next;
  }
  return NULL;
}

int main(int argc, char* argv[])
{
  int a[] = {1,2,3,4,5,3};
  s_node* root = create_linked_list(a,6);
  s_node* tail = get_first_node(root,5);
  s_node* node = get_first_node(root,3);
  append_node(root,node);
  s_node* loop_head = get_first_loop_head(root);
  if ( loop_head )
    printf("%d\n", loop_head->data);
  tail->next = NULL;
  clear_linked_list(root);
}
