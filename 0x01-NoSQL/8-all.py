#!/usr/bin/env python3
"""
list_all -  lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    The function "list_all" returns all documents in a MongoDB collection.

    :param mongo_collection: The `mongo_collection` parameter is expected
                             to be a collection object from a
                             MongoDB database.
    :return: the result of the `find()` method called on
             the `mongo_collection` object.
    """
    return mongo_collection.find()
