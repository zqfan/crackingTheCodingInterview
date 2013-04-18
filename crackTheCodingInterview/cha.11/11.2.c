/* 11.2
   You are given the source to an application which crashes when it is
   run. After running it ten times in a debugger, you find it never
   crashes in the same place. The application is single threaded, and
   uses only the C standard library. What programming errors could be
   causing this crash? How would you test each one?

   Analyse:
   1. resource error: the program read some resource uri from user's
   input, but sometimes that resource is not accessable. like url,
   file, memory alloc and etc.
   2. invalid access: the program use pointer or some handler, and
   release them but not reset them, and somewhere use them again. or
   just access invalid address due to wrong pointer.
   3. dependency: this program depends on particular CPU architecture,
   GPU, or some hardware like these. Or depends on runtime library.
*/
