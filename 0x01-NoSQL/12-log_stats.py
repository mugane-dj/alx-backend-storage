#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_count = nginx_collection.count_documents({})
    method_get = nginx_collection.count_documents({"method": "GET"})
    method_post = nginx_collection.count_documents({"method": "POST"})
    method_put = nginx_collection.count_documents({"method": "PUT"})
    method_patch = nginx_collection.count_documents({"method": "PATCH"})
    method_delete = nginx_collection.count_documents({"method": "DELETE"})
    status_check = nginx_collection.count_documents({"path": "/status"})
    print("{} logs".format(log_count))
    print("Methods:")
    print("\tmethod GET: {}".format(method_get))
    print("\tmethod POST: {}".format(method_post))
    print("\tmethod PUT: {}".format(method_put))
    print("\tmethod PATCH: {}".format(method_patch))
    print("\tmethod DELETE: {}".format(method_delete))
    print("{} status check".format(status_check))
