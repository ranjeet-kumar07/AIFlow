from app.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):

    def name(self) -> str:

        return "calculator"

    def description(self) -> str:

        return (
            "Performs arithmetic calculations."
        )

    def execute(
        self,
        arguments: dict
    ) -> str:

        expression = arguments.get(
            "expression",
            ""
        )

        try:

            result = eval(
                expression,
                {"__builtins__": {}},
                {}
            )

            return str(result)

        except Exception as ex:

            return (
                f"Calculation failed: {str(ex)}"
            )