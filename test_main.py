from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.post("/sentences_transformator",  json=["This framework generates embeddings for each input sentence"])
    assert response.status_code == 200
    response_body = response.json()[0]
    assert response_body['sentence'] == "This framework generates embeddings for each input sentence"
    assert response_body['embedding'][0] == 0.19731508195400238