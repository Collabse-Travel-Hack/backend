from http import HTTPStatus

from fastapi import HTTPException


class BadRequest(HTTPException):
    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST):
        super().__init__(status_code=status_code, detail=message)
