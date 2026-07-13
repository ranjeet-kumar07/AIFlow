from typing import Optional

from pydantic import BaseModel

from app.models.chat_response import ChatResponse
from app.models.tool_call import ToolCall


class ProviderResponse(BaseModel):

    chat_response: Optional[ChatResponse] = None

    tool_call: Optional[ToolCall] = None