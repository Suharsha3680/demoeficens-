#!/usr/bin/env python
# coding: utf-8

# In[14]:
import sys
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connect_cassandra(cluster_address, username, password):
    auth_provider = PlainTextAuthProvider(username=username, password=password)
    cluster = Cluster([cluster_address], auth_provider=auth_provider)
    session = cluster.connect()
    return session

def collect_metrics(session):
    metrics = {}

    # Collect and store metrics here

    return metrics

def display_metrics(metrics):
    for key, value in metrics.items():
        print(f"{key}: {value}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python cassandra_metrics.py <cluster_address> <username> <password>")
        sys.exit(1)

    cluster_address = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    session = connect_cassandra(cluster_address, username, password)
    metrics = collect_metrics(session)
    display_metrics(metrics)

if __name__ == "__main__":
    main()

# In[ ]:




