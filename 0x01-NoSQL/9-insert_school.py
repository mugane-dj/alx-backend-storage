#!/usr/bin/env python3
"""
insert_school - inserts a new document in a collection
                based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    The function `insert_school` inserts a document into a MongoDB
    collection with the provided key-value pairs.

    :param mongo_collection: The `mongo_collection` parameter is
                            the collection in the MongoDB database
    :return: the result of the `insertOne` method called on the
             `mongo_collection` object.
    """
    obj = {}
    for k, v in kwargs.items:
        obj[k] = v
    return mongo_collection.insert_one(obj).inserted_id
