#include <stdlib.h>
#include <stdio.h>
#include "link.h"
#include "dbg.h"

s_node* create_node(int data)
{
  s_node* node = (s_node*)malloc(sizeof(s_node));
  check_mem(node);
  node->data = data;
  node->next = NULL;
  return node;
 error:
  return NULL;
}

s_node* create_linked_list(const int* data, int len)
{
  s_node* root = NULL;
  s_node* cur = NULL;
  s_node* next = NULL;
  int i;
  if ( len < 1 )
    return NULL;
  root = create_node(data[0]);
  check_mem(root);
  cur = root;
  for ( i = 1; i < len; i++ ) {
    next = create_node(data[i]);
    cur->next = next;
    cur = next;
  }
  return root;
 error:
  clear_linked_list(root);
  return NULL;
}

int clear_linked_list(s_node* root)
{
  s_node* tmp = NULL;
  while ( root ) {
    tmp = root;
    root = root->next;
    free(tmp);
  }
  return 0;
}

int delete_node(s_node* root, s_node* target)
{
  if ( NULL == target )
    return 0;
  if ( root == target ) {
    root = root->next;
    free(target);
    return 0;
  }
  s_node* tmp = root;
  while ( tmp ) {
    if ( tmp->next == target ) {
      tmp->next = target->next;
      free(target);
      return 0;
    }
    tmp = tmp->next;
  }
  return 1;
}

void print_linked_list(s_node* root)
{
  s_node* tmp = root;
  while ( tmp ) {
    printf("%d ",tmp->data);
    tmp = tmp->next;
  }
  printf("\n");
}

s_node* get_first_node(s_node* root, int data)
{
  s_node* tmp = root;
  while ( tmp ) {
    if ( tmp->data == data )
      return tmp;
    tmp = tmp->next;
  }
  return NULL;
}

void append_node(s_node* root, s_node* node)
{
  s_node* tmp = root;
  while ( tmp ) {
    if ( NULL == tmp->next ) {
      tmp->next = node;
      return;
    }
    tmp = tmp->next;
  }
}
