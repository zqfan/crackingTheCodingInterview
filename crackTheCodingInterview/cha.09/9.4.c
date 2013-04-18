/* 9.4
   If you have a 2 GB file with one string per line, which sorting
   algorithm would you use to sort the file and why? */

/* read part of it, for example, 10 MB, sort it and write to a tmp
   file. then merge all tmp file to a large file.
   if a line's head in nth part, then the line belong to the nth part.
   then the next part will seek to the previous one's end.

   this method can avoid the situation that RAM is not enough. */
