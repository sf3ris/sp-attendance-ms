from typing import Dict
from mongoengine import (
    Document,
    DateTimeField,
    StringField,
    ListField,
)


class Attendance(Document):

    date = DateTimeField(required=True)
    type = StringField()
    athletes_ids = ListField(field=StringField())
    members_ids = ListField(field=StringField())
    title = StringField(required=True)

    def jsonify(self) -> Dict[str, str]:
        attendance = super().to_mongo()
        if '_id' in attendance:
            attendance['_id'] = str(attendance['_id'])

        return attendance
