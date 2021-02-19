from typing import List
from flask.json import jsonify
from flask.wrappers import Response, Request
from werkzeug.exceptions import abort
from model.attendance_model import Attendance
import sys
import bson


class AttendanceController():

    ATTENDANCE_DATE_KEY = 'date'
    ATTENDANCE_TYPE_KEY = 'type'
    ATTENDANCE_MEMBERS_IDS_KEY = 'members_ids'
    ATTENDANCE_ATHLETES_IDS_KEY = 'athletes_ids'
    ATTENDANCE_TITLE_KEY = 'title'

    def __init__(self) -> None:
        pass

    def post_attendance(self, req: Request) -> Response:
        """Validates request inputs and create an attendance Document

        Args:
            req (Request): Flask's HTTP Request

        Returns:
            Response: Response containing Attendance created document
        """
        attendance_date = req.form.get(self.ATTENDANCE_DATE_KEY)
        attendance_type = req.form.get(self.ATTENDANCE_TYPE_KEY)
        attendance_title = req.form.get(self.ATTENDANCE_TITLE_KEY)
        members_ids = req.form.get(self.ATTENDANCE_MEMBERS_IDS_KEY)
        athletes_ids = req.form.get(self.ATTENDANCE_ATHLETES_IDS_KEY)

        if members_ids is not None:
            members_ids = members_ids.split(",")
        if athletes_ids is not None:
            athletes_ids = athletes_ids.split(",")

        print(athletes_ids, file=sys.stderr)
        print(members_ids, file=sys.stderr)
        attendance: Attendance = Attendance(
            date=attendance_date,
            type=attendance_type,
            athletes_ids=athletes_ids,
            members_ids=members_ids,
            title=attendance_title
        )

        attendance.save()

        return jsonify(attendance.jsonify())

    def put_attendance(self, req: Request, attendance_id: int) -> Response:
        """Validates request inputs and update an attendance Document

        Args:
            req (Request): Flask's HTTP Request

        Returns:
            Response: Response containing Attendance updated document
        """
        if not bson.ObjectId.is_valid(attendance_id):
            abort(400)

        attendance_title = req.form.get(self.ATTENDANCE_TITLE_KEY)
        members_ids = req.form.get(self.ATTENDANCE_MEMBERS_IDS_KEY)
        athletes_ids = req.form.get(self.ATTENDANCE_ATHLETES_IDS_KEY)

        attendance = Attendance.objects(id=attendance_id).first()
        if not attendance:
            abort(404)

        if attendance_title is not None:
            attendance.title = attendance_title
        if members_ids is not None:
            members_ids = members_ids.split(",")
            attendance.members_ids = members_ids
        if athletes_ids is not None:
            athletes_ids = athletes_ids.split(",")
            attendance.athletes_ids = athletes_ids

        attendance.save()

        return jsonify(attendance.jsonify())

    def get_attendances(self, req: Request) -> Response:
        """Retrieves all attendance documents

        Args:
            req (Request): Flask's HTTP Request

        Returns:
            Response: List of Attendances
        """
        attendances: List[Attendance] = Attendance.objects().all()

        return jsonify(list(map(lambda x: x.jsonify(), attendances)))

    def get_attendance(self, req: Request, attendance_id: int) -> Response:
        """Retrieve the requested attendance documment

        Args:
            req (Request): Flask's HTTP Request
            attendance_id (int): requested attendance id

        Returns:
            Response: requested Attendance document
        """
        if not bson.ObjectId.is_valid(attendance_id):
            abort(400)

        attendance = Attendance.objects(id=attendance_id).first()
        if not attendance:
            abort(404)

        return jsonify(attendance.jsonify())

    def delete_attendance(self, req: Request, attendance_id: int) -> Response:
        """Delete the attendance

        Args:
            req (Request): Flask's HTTP Request
            attendance_id (int): requested attendance id

        Returns:
            Response: Response of delete process
        """
        if not bson.ObjectId.is_valid(attendance_id):
            abort(400)

        attendance = Attendance.objects(id=attendance_id).first()
        if not attendance:
            abort(404)
        
        attendance.delete()

        return ""
