/* 11.3
   We have the following method used in a chess game: boolean
   canMoveTo(int x, int y) x and y are the coordinates of the chess
   board and it returns whether or not the piece can move to that
   position. Explain how you would test this method.

   Analyze:
   1. invalid parameter:
   x or/and y is less than 0;
   x or/and y is larger or equal than 8 (or the chess board edge)
   2. valid parameter:
   select some coordinates for a piece which can move to and cannot
   move to, check if the return is correct. */
