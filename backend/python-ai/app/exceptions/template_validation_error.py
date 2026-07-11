class TemplateValidationError(Exception):

    def __init__(
        self,
        missing_variables: list[str]
    ):
        self.missing_variables = missing_variables

        super().__init__(
            "Missing template variables: "
            + ", ".join(missing_variables)
        )