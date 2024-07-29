#!/usr/bin/env python3
"""
Main file to test the Cache class.
"""

import redis
from exercise import Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    retrieved_value = cache.get(key, fn=fn)
    assert retrieved_value == value, f"Expected {value}, got {retrieved_value}"

print("All test cases passed!")
