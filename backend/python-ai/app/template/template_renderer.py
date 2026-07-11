class TemplateRenderer:

    @staticmethod
    def render(
        template: str,
        variables: dict[str, str]
    ) -> str:

        rendered = template

        for key, value in variables.items():
            rendered = rendered.replace(
                f"{{{{{key}}}}}",
                str(value)
            )

        return rendered