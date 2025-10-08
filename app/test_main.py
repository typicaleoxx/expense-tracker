from fastapi.testclient import TestClient
from main import app  #import your fast API app
client = TestClient(app)

#Test for the /hello endpoint 

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello, World!"}

def test_create_item():
    response = client.post("/items/", json={"name":"Book", "price":15.5, "description":"A sci-fi novel"})
    print(response.json())
    assert response.status_code==200
    assert response.json() == {
    "message":"Item created successfully!",
    "item":{
        "name":"Book",
        "price":15.5,
        "description":"A sci-fi novel"
    }
    }