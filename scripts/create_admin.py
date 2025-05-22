from users.models import User
import environ

def create_admin():
    environ.Env.read_env()
    env = environ.Env()
    username = env('APP_USERNAME')
    email = env('APP_EMAIL')
    password = env('APP_PASSWORD')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            user_type= User.UserType.ADMIN
        )
    else:
        pass
