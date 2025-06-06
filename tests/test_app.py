from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root():
    """
    Esse teste tem 3 etapas
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUT)
    - A: Assert  - Garante que A é A
    """

    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Welcome to the Fast Zero API!'}
