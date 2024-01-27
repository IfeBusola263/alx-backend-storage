#!/usr/bin/env python3
'''
This script provides a log on some statistics about Nginx saved
on MongoDB.

94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
'''

from pymongo import MongoClient
if __name__ == "__main__":

    # Connecting with MongoDB with pymongo
    client = MongoClient('mongodb://127.0.0.1:27017')

    # logs is the collection and nginx is document
    nginx_collection = client.logs.nginx

    # Query for some paramters
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:\n\tmethod GET: {}\n\t'
          'method POST: {}\n\t'
          'method PUT: {}\n\t'
          'method PATCH: {}\n\t'
          'method DELETE: {}'.format(
              nginx_collection.count_documents({'method': 'GET'}),
              nginx_collection.count_documents({'method': 'POST'}),
              nginx_collection.count_documents({'method': 'PUT'}),
              nginx_collection.count_documents({'method': 'PATCH'}),
              nginx_collection.count_documents({'method': 'DELETE'})))
    print('{} status check'.format(
        nginx_collection.count_documents({'path': '/status'})))

    list_of_ips = nginx_collection.aggregate([
        {
            '$group': {
                '_id': '$ip',
                'count': {'$sum': 1}
                }
        },
        {
            '$sort': {'count': -1}
        },
        {
            '$limit': 10
        }
        ])
    print('IPs:')
    for doc in list_of_ips:
        print(f'\t{doc["_id"]}: {doc["count"]}')
