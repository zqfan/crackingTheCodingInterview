"""
What is the difference between final, finally, and finalize?

Analyze:
in java,
## final
* final var: value is const
* final class: class cannot be inherited
* final method: method cannot be overridden

## finally
try-catch-finally block, no matter what happens in try or/and catch
block, statements in finally block will be executed

## finalize
jvm will run Finalize() method before running GC
"""
