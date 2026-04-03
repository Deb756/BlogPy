from django.db import models
from mongoengine import*
import datetime 

# Create your models here.
class Users(Document):
    uname = StringField(required=True)
    email = StringField(required=True,unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
