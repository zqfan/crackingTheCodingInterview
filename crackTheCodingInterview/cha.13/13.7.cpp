/* 13.7
   Why does a destructor in base class need to be declared virtual?

   Analyze:
   if a base class's destructor is not declared virtual, image that, a
   careless programmer derived from that class, allocate some
   resource, but forget to free them, and when the sub class is
   destroyed, the compiler cannot find this problem but will cause
   run-time error or memory leak and so on.

   WRONG !!!
   Calling a method with an object pointer always invokes:
   * the most derived class function, if a method is virtual.
   * the function implementation corresponding to the object pointer
   type (used to call the method), if a method is non-virtual.

   If we call delete on a base pointer which points to a derived class
   object, the base class destructor gets called first (for
   non-virtual function). If we declare the base class destructor as
   virtual, this makes all the derived class destructors virtual as
   well. So we should use virtual destructors if we call delete on a
   base class pointer which points to a derived class.
*/
