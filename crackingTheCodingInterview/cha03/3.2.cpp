/* How would you design a stack which, in addition to push and pop,
   also has a function min which returns the minimum element? Push,
   pop and min should all operate in O(1) time.

   Analyse:
   If i want to save time, i use more space. Using linked list
   implement the stack, then use a seperate pointer to point to the
   minimum element, every push will exa
   Oh, no. I think there is no such way to implement it. Since sort()
   cannot faster than O(nlogn), if i implement this, i will push a
   array to this stack, and use min() to sort it, and i get a O(n)
   sort(). I don't think it will happen.

   Oops, i was wrong.
   because i just need to know which is the minimize, but that one
   can not be at the top of the stack, it can be anywhere in the
   middle of the stack.
*/
#include <iostream>
#include <stack>
using namespace std;

template<class T>
class MinStack
{
public:
  stack<T> min_stack;
  stack<T> data_stack;
  MinStack(){};
  ~MinStack(){};
  void push(T value);
  T pop();
  const T& min();
  bool empty();
};

template<class T>
void MinStack<T>::push(T value)
{
  data_stack.push(value);
  if (min_stack.empty() || value < min_stack.top())
    min_stack.push(value);
}

template<class T>
T MinStack<T>::pop()
{
  if (data_stack.top() == min_stack.top())
    min_stack.pop();
  return data_stack.pop();
}

template<class T>
const T & MinStack<T>::min()
{
  return min_stack.top();
}

template<class T>
bool MinStack<T>::empty()
{
  return data_stack.empty();
}

int main()
{
  MinStack<int> ms;
  ms.push(1);
  ms.push(2);
  cout << ms.min() << endl;
  return 0;
}
