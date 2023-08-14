#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    nginx_collection = client.logs.nginx
    log_count = nginx_collection.count_documents({})
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} logs".format(log_count))
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: nginx_collection.count_documents({"method": method}) for method in http_methods}
    for method, count in method_counts.items():
        print("\tmethod {}: {}".format(method, count))
    print("{} status check".format(status_check))
    client.close()
