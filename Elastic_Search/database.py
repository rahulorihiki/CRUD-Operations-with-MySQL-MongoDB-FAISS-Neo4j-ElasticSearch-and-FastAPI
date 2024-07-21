from elasticsearch import Elasticsearch, NotFoundError


def create_connection():
    es = Elasticsearch(
        [{"host": "localhost", "port": 9200, "scheme": "https"}],
        verify_certs=False,
        http_auth=("elastic", "elastic"),
    )
    return es


def create_document(es, index, id, body):
    es.index(index=index, id=id, body=body)


def read_document(es, index, id):
    try:
        return es.get(index=index, id=id)
    except NotFoundError:
        return None


def update_document(es, index, id, body):
    es.update(index=index, id=id, body={"doc": body})


def delete_document(es, index, id):
    es.delete(index=index, id=id)
