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
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
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
