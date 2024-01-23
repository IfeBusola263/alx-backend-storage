#!/usr/bin/env python3
'''
This module has a function to update some collections
based on the name field of the documents in the collection.
'''

def update_topics(mongo_collection, name, topics):
    '''
    The function changes the topics of a school collection document
    (mongo_collection) based on the field 'name' to the list of topics
    'topics'.
    '''


    result = mongo_collection.update_one({'name': name},
                                          {'$set': {'topics': topics}})
