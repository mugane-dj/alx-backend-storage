#!/usr/bin/env python3
"""
Cache class - A redis instance
count_calls - A function that counts how many times a function
              has been called
call_history - A function that stores the history of inputs and outputs
               for a particular function
replay - A function that displays the history of calls of a particular function
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    The `count_calls` function is a decorator that counts the
    number of times a method is called and stores the count in a
    Redis database.

    :param method: The `method` parameter is a callable object,
                   such as a function or method, that we want to
                   count the number of times it is called
    :type method: Callable
    :return: The `count_calls` function returns a wrapper function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    The `call_history` function is a decorator that logs the inputs
    and outputs of a method to a Redis database.

    :param method: The `method` parameter is a callable object,
                   such as a function or method, that we want to
                   wrap with the `call_history` decorator
    :type method: Callable
    :return: The function `call_history` returns a wrapper function
             `wrapper`.
    """
    @wraps(method)
    def wrapper(self, *args):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    The `replay` function retrieves information from a Redis
    database to display the number of times a method was called
    and the corresponding inputs and outputs.

    :param method: The `method` parameter is expected to be a
                   callable object, such as a function or a method.
                   It should be a function that you want to replay
                   and print the details of its previous
    invocations
    :type method: Callable
    """
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name).decode('utf-8')
    inputs = r.lrange(method_name + ":inputs", 0, -1)
    outputs = r.lrange(method_name + ":outputs", 0, -1)
    print(f"{method_name} was called {count} times:")
    for k, v in zip(inputs, outputs):
        print(f"{method_name}(*({k.decode()},)) -> {v.decode('utf-8')}")


class Cache:
    def __init__(self):
        """
        Initialize a Cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The `store` function takes in data of type `str`, `bytes`,
        `int`, or `float`, generates a unique key using `uuid.uuid4()`,
        stores the data in Redis using the generated key, and returns the key.

        :param data: The `data` parameter can be of type `str`, `bytes`,
                     `int`, or `float`. It represents the data that you
                     want to store in the Redis database
        :type data: Union[str, bytes, int, float]
        :return: a string, which is the key generated for storing the
                 data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[bytes, str, int]:
        """
        The `get` function retrieves a value from Redis using a given key,
        and optionally applies a function to the value before returning it.

        :param key: The `key` parameter is a string that represents the key
                    of the value to retrieve from the Redis database
        :type key: str
        :param fn: The `fn` parameter is a callable function that can be
                   passed as an argument to the `get`method. It is an optional
                   parameter, meaning it can be omitted when calling the method
        :type fn: Callable
        :return: The method `get` returns the value associated with the given
                 key in the Redis database.
        """
        value = self._redis.get(key)
        if value is None:
            return None

        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        The `get_str` function retrieves a value from a dictionary
        using a given key and converts it to a string using the `decode`
        method with the 'utf-8' encoding.

        :param key: The `key` parameter is a string that represents the
                    key used to retrieve the value.
        :type key: str
        :return: The `get_str` method returns a string.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        The function `get_int` returns the value associated with a given
        key as an integer.

        :param key: The `key` parameter is a string that represents the
                    key of the value you want to retrieve from a dictionary
        :type key: str
        :return: The `get_int` method is returning an integer value.
        """
        return self.get(key, fn=int)
