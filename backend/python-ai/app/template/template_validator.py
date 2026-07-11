import re
from app.exceptions.template_validation_error import (
    TemplateValidationError
)

class TemplateValidator:

    @staticmethod
    def validate(
        template: str,
        variables: dict
    ):

        placeholders = set(
            re.findall(
                r"\{\{(.*?)\}\}",
                template
            )
        )

        missing = placeholders - set(
            variables.keys()
        )

        if missing:
            raise TemplateValidationError(
                sorted(missing)

            )