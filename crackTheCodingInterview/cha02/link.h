#ifndef __LINK_H__
#define __LINK_H__

typedef struct NODE {
  int data;
  struct NODE* next;
} s_node;

s_node* create_node(int data);
s_node* create_linked_list(const int* data, int len);
int clear_linked_list(s_node* root);
int delete_node(s_node* root, s_node* target);
void print_linked_list(s_node* root);
s_node* get_first_node(s_node* root, int data);
void append_node(s_node* root, s_node* node);

#endif
