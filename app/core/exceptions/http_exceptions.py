from typing import Any

from fastapi import HTTPException

class BadRequestException(HTTPException):
    def __init__(self, detail: Any = None, msg: str = 'Bad Request.'):
        self.status_code = 400
        self.detail = {
            'status_code': 400,
            'data': detail,
            'msg': msg
        }

class UnauthorizedException(HTTPException):
    def __init__(self, detail: Any = None, msg: str = 'Not Authorized.'):
        self.status_code = 401
        self.detail = {
            'status_code': 401,
            'data': detail,
            'msg': msg
        }

class ForbiddenException(HTTPException):
    def __init__(self, detail: Any = None, msg: str = 'Forbidden.'):
        self.status_code = 403
        self.detail = {
            'status_code': 403,
            'data': detail,
            'msg': msg
        }


class InternalServerErrorException(HTTPException):
    def __init__(self, detail: Any = None, msg: str = 'Internal Server Error.'):
        self.status_code = 500
        self.detail = {
            'status_code': 500,
            'data': detail,
            'msg': msg
        }

class NotFoundException(HTTPException):
    def __init__(self, detail: Any = None, msg: str = 'Not Found.'):
        self.status_code = 404
        self.detail = {
            'status_code': 404,
            'data': detail,
            'msg': msg
        }

class HttpSuccessException(HTTPException):
    def __init__(self, detail: Any = None, msg: str = ''):
        self.status_code = 200
        self.detail = {
            'status_code': 400,
            'data': detail,
            'msg': msg
        }