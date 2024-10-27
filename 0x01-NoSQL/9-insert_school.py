#!/usr/bin/env python3

"""using mongo_collection as pymogo collection"""


def insert_school(mongo_collection, **kwargs):
    """ insert a new document in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)
