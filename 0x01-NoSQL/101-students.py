#!/usr/bin/env python3
'''
This module houses a function that returns students sorted by average
score.
'''

def top_students(mongo_collection):
    '''
    The function return a list of all the students sorted by
    the average score.
    '''

    # Query each student and add their scores to get the aggregate
    return mongo_collection.aggregate([
        {"$unwind": "$topics"}, # get the topic array out first
        {"$group": { "_id": "$_id",
                   "name": {"$first": "$name"},
                   "averageScore": {"$avg": "$topics.score"}}
         },
        {"$sort": {"averageScore": -1}}
        ])
    # update the document with the average calculation
