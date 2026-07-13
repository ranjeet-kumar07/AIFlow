from app.tools.tool_registry import TOOL_REGISTRY


class ToolMetadata:

    @staticmethod
    def list_tools() -> list[dict]:

        tools = []

        for tool_class in TOOL_REGISTRY.values():

            tool = tool_class()

            tools.append({

                "name": tool.name(),

                "description": tool.description()

            })

        return tools