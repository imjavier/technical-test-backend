from users.models import User

def create_users():
    User.objects.filter(user_type=User.UserType.EXTERNAL).delete()
    users = [
        {
            'username': 'user1',
            'email': 'javier@gmail.com',
            'password': 'password123',
        },
        {
            'username': 'user2',
            'email': 'maria@gmail.com',
            'password': 'password456',
        },
        {
            'username': 'user3',
            'email': 'carlos@gmail.com',
            'password': 'password789',
        },
        {
            'username': 'user4',
            'email': 'ana@gmail.com',
            'password': 'passwordabc',
        },
        {
            'username': 'user5',
            'email': 'luis@gmail.com',
            'password': 'passworddef',
        },
        {
            'username': 'user6',
            'email': 'sofia@gmail.com',
            'password': 'passwordghi',
        },
    ]
    for user in users:
        User.objects.create_user(
            username=user['username'],
            email=user['email'],
            password=user['password'],
            user_type=User.UserType.EXTERNAL
        )
