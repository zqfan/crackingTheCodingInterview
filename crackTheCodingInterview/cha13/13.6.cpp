/* 13.6
   What is name hiding in C++?

   Analyze:
   Name hiding happens when you create a object without a reference or
   pointer to it, or when type cast, or when complex value pass on
   function call.

   WRONG!!!
   In C++, when you have a class with an overloaded method, and you
   then extend and override that method, you must override all of the
   overloaded methods. Otherwise, the un-overrided methods will
   invisible. This is called name hiding.
*/
