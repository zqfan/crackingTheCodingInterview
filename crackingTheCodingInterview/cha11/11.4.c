/* 11.4
   How would you load test a webpage without using any test tools?

   Analyze:
   1) test for single access:
   if the ui has any problem?
   if the function has any problem?
   is it response fast?
   is it friendly when user input invalid data?
   2) test for max load:
   write concurrence multi-thread program, to simulate many users,
   each thread will record its latency, and amount of data fetched.
   increasing the thread number until one of them timeout to get
   request or server down.
   3) test for average load:
   the average is not just the middle, but the response time
*/
