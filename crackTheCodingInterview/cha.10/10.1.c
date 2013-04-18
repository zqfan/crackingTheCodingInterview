/* 10.1	 You have a basketball hoop and someone says that you can play
   1 of 2 games.
   Game #1: You get one shot to make the hoop.
   Game #2: You get three shots and you have to make 2 of 3 shots.
   If p is the probability of making a particular shot, for which
   values of p should you pick one game or the other?

   Analyse:
   for each shots, they are independent, so C(2,3)*p*p*(1-p)
   + C(3,3)*p*p*p > p => 3*p(1-p) + p*p > 1 ==> 3*p - 2*p*p - 1 > 0
   ==> 2*p*p - 3*p + 1 < 0 ==> (2p - 1)(p - 1) < 0 ==> p > 0.5
   so if p > 0.5, you should pick game 2 */
