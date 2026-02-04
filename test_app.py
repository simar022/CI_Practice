import pytest
from app import app

@pytest.fixture
def client():
    # Set up the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the default JSON response."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Flask is running in CI/CD!"}

def test_404_page(client):
    """Test that a non-existent route returns 404."""
    response = client.get('/non-existent')
    assert response.status_code == 404
