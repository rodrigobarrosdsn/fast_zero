from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        user = User(username='testuser', email='test@test.com')

        session.add(user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'testuser'))

    assert asdict(user) == {
        'id': 1,
        'username': 'testuser',
        'email': 'test@test.com',
        'created_at': time,
        'updated_at': time,
    }
