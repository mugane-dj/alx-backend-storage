#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all


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
    print(
        f"""{log_count} logs
Methods:
    method GET: {method_get}
    method POST: {method_post}
    method PUT: {method_put}
    method PATCH: {method_patch}
    method DELETE: {method_delete}
{status_check} status check"""
    )
