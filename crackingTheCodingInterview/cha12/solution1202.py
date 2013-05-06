"""
You are given the source to an application which crashes when it is run. After running it ten times in a debugger, you find it never crashes in the same place. The application is single threaded, and uses only the C standard library. What programming errors could be causing this crash? How would you test each one?

Analyze:
* only specific value will crash
* some env or library is missing when crash but your debugger has
* resource limitation, specific memory or multi-cpu is needed while client doesn't meet it
"""
