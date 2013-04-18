/* 11.1	 Find the mistake(s) in the following code:
   unsigned int i;
   for (i = 100; i <= 0; --i)
       printf(“%d\n”, i);

   Analyse:
   1. it should in a function
   2. it should include stdio.h
   3. the printf will never reach because 100 > 0
   4. i will never less than 0, since it is unsigned int.
   5. %d has a hidden cast, use %u instead
*/
