#!/usr/bin/env python3
'''
This module houses a function to that returns a lists of schools
based on the topics offered.
'''

def schools_by_topic(mongo_collection, topic):
    '''
    The function returns a list of the schools in the collection's documents
    having a specific topic.
    '''

    return [doc for doc in mongo_collection.find({'topics': {'$in': [topic]}})]

