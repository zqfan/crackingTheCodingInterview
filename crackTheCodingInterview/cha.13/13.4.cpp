/* 13.4
   What is the difference between deep copy and shallow copy? Explain
   how you would use each.

   Analyze:
   Deep copy will copy all data, shallow copy just copy the reference,
   so if the source data is changed, the copy is changed too. it seems
   similar to soft link and hard link on Linux.

   Shallow copy is dangerous, because when you release the reference,
   the shallow copy still hold even try to use it, this will cause
   run-time error, but shallow copy is still useful when pass a
   reference instead all data, this means it can save memory space and
   much faster.
*/
