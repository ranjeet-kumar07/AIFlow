## Why a WorkflowResolver?

Without a resolver, the Gateway would need multiple if/else statements to decide which prompt workflow to use.

The WorkflowResolver centralizes that decision, making it easier to extend the platform with additional AI workflows while keeping the Gateway simple.