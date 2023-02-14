from django.db import models
from django.contrib.auth.models import AbstractUser



# расширение кастомной юзер модели
class User_model(AbstractUser):
    pass

    class Meta():
        db_table = 'Users'
