from app.models.chat_request import ChatRequest
from app.workflow.workflow_registry import (
    WORKFLOW_REGISTRY,
)


class WorkflowResolver:

    @staticmethod
    def resolve(
        request: ChatRequest
    ) -> dict:

        workflow = request.workflow.lower()

        if workflow not in WORKFLOW_REGISTRY:

            raise ValueError(
                f"Unsupported workflow: {workflow}"
            )

        return WORKFLOW_REGISTRY[
            workflow
        ]