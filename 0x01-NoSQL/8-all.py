#!/usr/bin/env python3
'''
This is module houses functions for pymongo.
'''

def list_all(mongo_collection):
    '''
    This function returns an empty list if mongo_collections has no
    document, otherwise lists all the documents.
    '''

    if mongo_collection is None:
        return []

    return [doc for doc in mongo_collection.find()]
