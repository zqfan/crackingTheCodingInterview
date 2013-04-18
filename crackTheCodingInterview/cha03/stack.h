#ifndef __STACK_H__
#define __STACK_H__

struct {
  int s[100] = {0};
  int top = -1;
} s_stack;

int top(s_stack *s);
/* if empty, return -1; else return -1 */
int pop(s_stack *s);
/* if full, return -1; else return 0 */
int push(s_stack *s);

struct {
  s_stack stack;
  s_stack_node *next = NULL;
} s_stack_node;

struct {
  s_stack_node *root = NULL;
  s_stack_node *cur = NULL;
  int top();
  int pop();
  int push();
} s_stack_set;

int top(s_stack_set *s);

#endif
