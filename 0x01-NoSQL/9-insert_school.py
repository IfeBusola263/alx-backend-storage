#!/usr/bin/env python3
'''
This module house a function for pymongo.
'''

def insert_school(mongo_collection, **kwargs):
    '''
    This function returns an id after the successful insertion of kwargs
    in the mongoDB collection 'mongo_collection'.
    '''
    insert_id = mongo_collection.insert_one(kwargs)
    return insert_id.inserted_id
