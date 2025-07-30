from fast_zero.models import User


def test_create_user():
    user = User(username='testuser', email='test@test.com')
    assert user.username == 'testuser'
