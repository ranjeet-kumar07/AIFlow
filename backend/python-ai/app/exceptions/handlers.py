from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.template_validation_error import (
    TemplateValidationError,
)
from app.services.observability_service import (
    ObservabilityService,
)


async def template_validation_exception_handler(
    request: Request,
    exc: TemplateValidationError,
):

    ObservabilityService.validation_failed(
        str(exc)
    )

    return JSONResponse(
        status_code=400,
        content={
            "error": "Template validation failed",
            "missing_variables": exc.missing_variables,
        },
    )