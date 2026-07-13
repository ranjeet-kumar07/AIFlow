from app.tools.base_tool import BaseTool
from app.tools.calculator_tool import CalculatorTool


class ToolRegistry:

    _registry: dict[str, type[BaseTool]] = {
        "calculator": CalculatorTool
    }

    @classmethod
    def get(
        cls,
        tool_name: str
    ) -> BaseTool:

        tool_class = cls._registry.get(
            tool_name
        )

        if tool_class is None:
            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return tool_class()