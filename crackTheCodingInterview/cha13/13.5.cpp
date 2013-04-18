/* 13.5
   What is the significance of the keyword “volatile” in C?

   Analyze:
   Volatile tells the compiler that the decorated variable can be
   modified from the out scope to avoid compiler optimize. so the
   compiler will not replace the variable with the current value and
   will insist to get value from the variable address.
*/
