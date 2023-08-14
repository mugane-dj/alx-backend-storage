#!/usr/bin/env python3
"""
update_topics - changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
