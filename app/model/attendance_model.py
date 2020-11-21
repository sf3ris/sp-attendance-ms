from typing import Dict
from mongoengine import Document, DateTimeField, StringField, ListField, IntField

class Attendance(Document):

    date  = DateTimeField( required=True)
    type  = StringField()
    ids   = ListField(field=IntField())

    def jsonify(self) -> Dict[str,str]:

        attendance = super().to_mongo()
        if '_id' in attendance:
            attendance['_id'] = str(attendance['_id'])

        return attendance
