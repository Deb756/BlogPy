from mongoengine import Document, StringField, DateTimeField,ReferenceField
import datetime
from users.models import Users

class Post(Document):
    user_id = ReferenceField(Users, required=True)
    title = StringField(required=True)
    content = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)


