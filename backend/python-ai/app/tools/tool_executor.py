from app.models.tool_call import ToolCall
from app.models.tool_result import ToolResult
from app.tools.tool_registry import ToolRegistry


class ToolExecutor:

    @staticmethod
    def execute(
        tool_call: ToolCall
    ) -> ToolResult:

        tool = ToolRegistry.get(
            tool_call.tool_name
        )

        result = tool.execute(
            tool_call.arguments
        )

        return ToolResult(
            tool_name=tool_call.tool_name,
            result=result
        )