/* 13.8
   Write a method that takes a pointer to a Node structure as a
   parameter and returns a complete copy of the passed-in data
   structure. The Node structure contains two pointers to other Node
   structures.

   Analyze:
   this source code copies from solution
*/

typedef map<Node *, Node *> node2node

Node * copy_recursive(Node * cur, node2node & node_map)
{
  if ( cur == NULL )
    return NULL;
  node2node::iterator i = node_map.find(cur);
  if ( i != node_map.end() )
    return i->second();
  Node * pnode = new Node;
  node_map[cur] = pnode;
  pnode->left = copy_recursive(cur->left, node_map);
  pnode->right = copy_recursive(cur->right, node_map);
  return pnode;
}

Node * copy_struct(Node * root)
{
  node2node node_map;
  return copy_recursive(root, node_map);
}
