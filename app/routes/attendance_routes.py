from flask import Blueprint
from flask.globals import request
from flask.wrappers import Response
from controller.attendance_controller import AttendanceController

attendance_routes = Blueprint('attendance_routes',__name__)

@attendance_routes.route('/attendances', methods=['GET'])
def get_attendances() -> Response:
    return AttendanceController().get_attendances( request )

@attendance_routes.route('/attendances', methods=['POST'])
def post_attendance() -> Response:
    return AttendanceController().post_attendance( request )

@attendance_routes.route('/attendances/<attendance_id>', methods=['GET'])
def get_attendance( attendance_id : int = 0 ) -> Response:
    return AttendanceController().get_attendance( request, attendance_id )
