/* You have two numbers represented by a linked list, where each node
   contains a single digit. The digits are stored in reverse order,
   such that the 1’s digit is at the head of the list. Write a
   function that adds the two numbers and returns the sum as a linked
   list.
   EXAMPLE
   Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
   Output: 8 -> 0 -> 8
*/
#include <stdlib.h>
#include "link.h"

s_node* add_linked_list(s_node* a, s_node* b)
{
  s_node* root = NULL;
  s_node* cur = NULL;
  int sum = 0;
  s_node* cur_a = a;
  s_node* cur_b = b;
  int extend = 0;
  while ( cur_a or cur_b ) {
    if ( NULL == cur_a )
      sum = 0;
    else
      sum = cur_a->data;
    if ( NULL != cur_b )
      sum += cur_b->data;
    sum += extend;
    extend = sum / 10;
    sum = sum % 10;
    if ( NULL == root ) {
      root = create_node(sum);
      cur = root;
    }
    else {
      cur->next = create_node(sum);
      cur = cur->next;
    }
    cur_a = cur_a->next;
    cur_b = cur_b->next;
  }
  return root;
}

int main(int argc, char* argv[])
{
  int a[] = {3,1,5};
  int b[] = {5,9,2};
  s_node* link_a = create_linked_list(a,3);
  s_node* link_b = create_linked_list(b,3);
  s_node* sum = add_linked_list(link_a, link_b);
  print_linked_list(sum);
  clear_linked_list(link_a);
  clear_linked_list(link_b);
  clear_linked_list(sum);
  return 0;
}
