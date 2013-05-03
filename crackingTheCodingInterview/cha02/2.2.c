/* Implement an algorithm to find the nth to last element of a singly
   linked list.

   Analyse:
   i think this problem doesn't mean sort it first and get the [n:-1]
*/
#include "link.h"

s_node* get_element(s_node* root, int start)
{
  s_node* tmp = root;
  while ( tmp && start > 0 ) {
    start--;
    tmp = tmp->next;
  }
  return tmp;
}

int main(int argc, char* argv[])
{
  int a[] = {1,2,3,4,5};
  s_node* root = create_linked_list(a,sizeof(a)/sizeof(a[0]));
  s_node* r = get_element(root, 3);
  print_linked_list(r);
  clear_linked_list(root);
  return 0;
}