from mongoengine import Document, StringField, DateTimeField
import datetime

class Post(Document):
    title = StringField(required=True)
    content = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)


