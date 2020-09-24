# Create your models here.
from django.db import models
import re
import bcrypt
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['first_name']) < 3:
            errors.append('First name must be more than 3 characters')
        if len(form_data['last_name']) < 3:
            errors.append('Last name must be more than 3 characters')
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append('Email address is in wrong format')
        user_list = self.filter(email=form_data['email'])
        if len(user_list) > 0:
            errors.append("Email already in use.")
        if len(form_data['pwd']) < 8:
            errors.append("Password too short.")
        return errors

    def create_user(self, form_data):
        pw_hash =bcrypt.hashpw(form_data['pwd'].encode('utf-8'), bcrypt.gensalt())
        return self.create(
            first_name = form_data['first_name'],
            last_name  = form_data['last_name'],
            email      = form_data['email'],
            pwd        = pw_hash.decode('utf-8')
        )

    def login(self, form_data):
        errors=[]
        #user = self.get(email=form_data['email'])
        existing_users = self.filter(email=form_data['email'])
        if not existing_users:
           errors.append("Email or password invalid")
        else:
           user = existing_users[0]
        print(form_data['pwd'])
        print(user.pwd)
        if bcrypt.checkpw(form_data['pwd'].encode('utf-8'), user.pwd.encode('utf-8')):
            return (True, user)
        else:
            return (False, "Email or password invalid")


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pwd = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()

    def __str__(self):
        return self.last_name + " " + self.first_name
