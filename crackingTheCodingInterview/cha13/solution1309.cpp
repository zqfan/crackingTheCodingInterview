/* Write a smart pointer (smart_ptr) class. */
#include <stdlib.h>

template<class T>
class SmartPointer {
protected:
  T * ref;
  unsigned * ref_count;
public:
  SmartPointer(T * ptr) {
    ref = ptr;
    ref_count = (unsigned*)malloc(sizeof(unsigned));
    *ref_count = 1;
  }
  SmartPointer(SmartPoint<T> & sptr) {
    ref = sptr.ref;
    ref_count = sptr.ref_count;
    ++*ref_count;
  }
  SmartPointer<T> & operator = (SmartPoint<T> & sptr) {
    if (this != sptr) {
      ref = sptr.ref;
      ref_count = sptr.ref_count;
      ++*ref_count;
    }
    return *this;
  }
  ~SmartPointer() {
    --*ref_count;
    if (*ref_count == 0) {
      delete ref;
      ref = NULL;
      free(ref_count);
      ref_count = NULL;
    }
  }
  T value() {
    return *ref;
  }
};
