#!/usr/bin/env python3

""" lists all documents in a collection using pymongo"""


def list_all(mongo_collection):
    """ list documents"""
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
