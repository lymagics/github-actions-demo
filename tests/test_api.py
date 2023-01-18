import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200

    data = response.json
    assert 'message' in data
    assert data['message'] == 'pong'
