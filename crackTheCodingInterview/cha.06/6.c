/* 6.1
 * Add arithmetic operators (plus, minus, times, divide) to make the
   following expression true: 3 1 3 6 = 8. You can use any parentheses
   you’d like.

   Analyse:
   (3+1)/(3/6) = 8

   6.2
   There is an 8x8 chess board in which two diagonally opposite
   corners have been cut off. You are given 31 dominos, and a single
   domino can cover exactly two squares.
   Can you use the 31 dominos to cover the entire board? Prove your
   answer (by providing an example, or showing why it’s impossible).

   Analyse:

   6.3
   You have a five quart jug and a three quart jug, and an unlimited
   supply of water (but no measuring cups). How would you come up with
   exactly four quarts of water?
   NOTE: The jugs are oddly shaped, such that filling up exactly
   ‘half’ of the jug would be impossible.

   Analyse:
   1. fill 3
   2. from 3 to 5, 3 empty
   3. fill 3
   4. from 3 to 5, 3 left 2
   5. fill 5,
   6. from 5 to 3, 5 left 4

   6.4
   A bunch of men are on an island. A genie comes down and gathers
   everyone together and places a magical hat on some people’s heads
   (i.e., at least one person has a hat). The hat is magical: it can
   be seen by other people, but not by the wearer of the hat himself.
   To remove the hat, those (and only those who have a hat) must dunk
   themselves underwater at exactly midnight. If there are n people
   and c hats, how long does it take the men to remove the hats?
   The men cannot tell each other (in any way) that they have a hat.
   FOLLOW UP
   Prove that your solution is correct.

   Analyse:
   I assume that:
   1. people are clever, they can judge correctly.
   2. people are honest, they will dunk themselves if they know they
   get a hat in their head.

   so if there is c hats, it will take c days to remove their hats,
   and that will happen exactly on c day.

   the man has a hat will see c-1 hats, if on c-1 day, those people
   don't dunk themselves, then the man will know he has a hat. if c=1,
   the man with a hat will see no hat, so he will dunk himself right
   on the first day.

   using mathematical induction to prove this:
   c = 1, it is right.
   assume c = n is right, then for c = n+1:
   on n day, no man dunks himself, so the man see n hats knows that
   there must exist more hats, so the only one must be himself, so he
   will dunk himself on the middlenight. since the man is selected
   randomly, so all man see n hats will do the same. so for c = n+1 is
   right too.

   6.5
   There is a building of 100 floors. If an egg drops from the Nth
   floor or above it will break. If it’s dropped from any floor below,
   it will not break. You’re given 2 eggs. Find N, while minimizing
   the number of drops for the worst case.

   Analyse:
   tough eggs.
   for 0 < M <= 100, it will divide the 100 floors to 100/M blocks,
   for the worst case, you will need N/M drops to test which block the
   N in, and will need N%M in range [1,M) drops (if N%M == 0: after
   M-1 drops will automatically know). so c = ceil(N/M) + {N%M for
   N%M!=0 |M-1 for N%M==0}, for the worst case, N%M==0, c = ceil(N/M)
   + M - 1, for the worst case N is very close to 100, so choose M=10,
   and it need 20 drops.

   6.6
   There are one hundred closed lockers in a hallway. A man begins by
   opening all one hundred lockers. Next, he closes every second
   locker. Then he goes to every third locker and closes it if it is
   open or opens it if it is closed (e.g., he toggles every third
   locker). After his one hundredth pass in the hallway, in which he
   toggles only locker number one hundred, how many lockers are open?

   Analyse:
*/
