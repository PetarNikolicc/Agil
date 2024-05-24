from app import app

def test_app():
    client=app.test_client()
    response  = client.get("/")
    assert response.text == 200
    