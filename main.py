from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

es.ping()

print(f"Connected to {es.info()}\n")
print(f"Ping: {es.ping()}\n")

