"""
How would you test an ATM in a distributed banking system?

Analyze:

* insert a bad card
* insert a good card but input wrong password
* after login or any operation, wait timeout seconds to see what will
happen
* try to get more money than account
* try to get same money of account have
* try to get more money than limit
* try to get money both from two ATM in the same time, but the sum is
less or equal than account
* try to get more money than account from multi ATM concurrency
* try any operation after ATM connection lost
* try same operation from e-bank (on the website) while operate on the
ATM
"""
