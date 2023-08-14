#!/usr/bin/env python3
"""
schools_by_topic - returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    The function "schools_by_topic" takes a MongoDB collection
    and a topic as input, and returns all documents in the collection
    that have the specified topic in their "topics" field.

    :param mongo_collection: A MongoDB collection object that represents
                             a collection of documents in a MongoDB database
    :param topic: The topic parameter is a string that represents the topic
                  you want to search for in the MongoDB collection
    :return: a cursor object that contains all the documents in the
             mongo_collection that have the specified topic in their
             "topics" field.
    """
    return mongo_collection.find({"topics": topic})
