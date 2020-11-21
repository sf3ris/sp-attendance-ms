from sys import stderr
from typing import List
from flask.json import jsonify
from flask.wrappers import Response, Request
from mongoengine.document import Document
from werkzeug.exceptions import abort
from model.attendance_model import Attendance

import bson

class AttendanceController():

    ATTENDANCE_DATE_KEY = 'date'
    ATTENDANCE_TYPE_KEY = 'type'
    ATTENDANCE_TYPE_IDS = 'ids'

    def __init__(self) -> None:
        pass
    
    
    def post_attendance(self, req : Request ) -> Response:
        """Validates request inputs and create an attendance Document

        Args:
            req (Request): Flask's HTTP Request

        Returns:
            Response: Response containing Attendance created document
        """    
        attendance_date = req.form.get(self.ATTENDANCE_DATE_KEY)
        attendance_type = req.form.get(self.ATTENDANCE_TYPE_KEY)
        attendance_ids  = list( int(id) for id in req.form.get(self.ATTENDANCE_TYPE_IDS).split(","))

        attendance : Attendance = Attendance(
            date = attendance_date, 
            type = attendance_type, 
            ids = attendance_ids
        )

        attendance.save()

        return jsonify( attendance.jsonify() )

    def get_attendances( self, req: Request ) -> Response:
        """Retrieves all attendance documents

        Args:
            req (Request): Flask's HTTP Request

        Returns:
            Response: List of Attendances
        """        

        attendances : List[Attendance] = Attendance.objects().all()

        
        return jsonify( list(map( lambda x : x.jsonify(), attendances) ))

    def get_attendance( self, req: Request, attendance_id : int ) -> Response:
        """Retrieve the requested attendance documment

        Args:
            req (Request): Flask's HTTP Request
            attendance_id (int): requested attendance id

        Returns:
            Response: requested Attendance document
        """        
        if not bson.ObjectId.is_valid( attendance_id ):
            abort(400)

        attendance = Attendance.objects(id=attendance_id).first()
        if not attendance:
            abort(404)

        return jsonify( attendance.jsonify() )
