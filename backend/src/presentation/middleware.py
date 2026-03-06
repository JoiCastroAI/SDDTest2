from fastapi import Request
from fastapi.responses import JSONResponse

from src.domain.exceptions import ConflictError, NotFoundError, ValidationError


async def domain_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    if isinstance(exc, NotFoundError):
        return JSONResponse(status_code=404, content={"error": {"message": str(exc), "code": "NOT_FOUND"}})
    if isinstance(exc, ValidationError):
        return JSONResponse(status_code=400, content={"error": {"message": str(exc), "code": "VALIDATION_ERROR"}})
    if isinstance(exc, ConflictError):
        return JSONResponse(status_code=409, content={"error": {"message": str(exc), "code": "CONFLICT"}})
    return JSONResponse(status_code=500, content={"error": {"message": "Internal server error", "code": "INTERNAL_ERROR"}})
