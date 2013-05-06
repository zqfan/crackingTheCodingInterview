"""
Find the mistake(s) in the following code:
unsigned int i;
for (i = 100; i <= 0; --i)
    printf(“%d\n”, i);

Analyze:

* i = 100 so i will never less or equal than 0
* i is unsigned int, i will never larger or equal than 0
"""
