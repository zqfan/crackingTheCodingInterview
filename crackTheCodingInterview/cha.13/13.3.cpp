#include <iostream>
using namespace std;

class A
{
 public:
  virtual int print_info()
  {
    cout << "I'm class A" << endl;
    return 0;
  }
};


class B: public A
{
 public:
  int print_info()
  {
    cout << "I'm class B" << endl;
    return 0;
  }
};


int main()
{
  A * a = new A();
  a->print_info(); // print A, because it is a pointer of A
  A * b = new B();
  // print B, because it is a pointer of A
  // but derived from A, so the dynamic binding is the B.print_info()
  b->print_info();
  A c = B();
  c.print_info(); // print A, because it is an object of A
  delete a;
  delete b;
  return 0;
}
