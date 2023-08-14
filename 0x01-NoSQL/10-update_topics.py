#!/usr/bin/env python3
"""
update_topics - changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    The function updates the "topics" field of documents in a MongoDB
    collection that match a given name.

    :param mongo_collection: The mongo_collection parameter is the
                             collection in MongoDB where the documents
                             are stored
    :param name: The name of the document you want to update in
                 the MongoDB collection
    :param topics: The `topics` parameter is a list of topics
                   that you want to update for a specific document in
                   the `mongo_collection`
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
