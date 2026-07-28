<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://github.com/pydantic/pydantic-ai/issues/3488 -->
<!-- Fetched: 2026-07-23 via defuddle CLI -->
<!-- NOTE: This is a GitHub feature-request issue on the pydantic-ai Python framework, NOT ServiceNow. Kept as prior-art on human-in-the-loop (HITL) approval design, conceptually relevant to agents like Proactive Customer Case Communicator (approve/modify/reject loop) even though the tech stack is unrelated. Not a ServiceNow source; use judgment before promoting into wiki/. -->
<!-- Fetched as part of a batch of 27 URLs; this is one of 4 that succeeded. -->

# pydantic-ai issue #3488 — Support `user_prompt` alongside HITL (human-in-the-loop)

### Description

Feature request: support `user_prompt` alongside HITL (human-in-the-loop approval).

The requester wants the Agent to receive user input *while* executing a command, to control its action direction and continue operations — i.e. real-time steering, not just binary approve/deny.

They note `ToolReturn.content` on `ToolApproved`/`ToolDenied` could achieve something similar, but feel supporting `user_prompt` directly is more natural.

### Example (illustrates the current binary approve/deny HITL pattern this issue wants extended)

```python
from pydantic_ai import (
    Agent,
    ApprovalRequired,
    DeferredToolRequests,
    DeferredToolResults,
    RunContext,
    ToolDenied,
)

agent = Agent('openai:gpt-5', output_type=[str, DeferredToolRequests])

PROTECTED_FILES = {'.env'}

@agent.tool
def update_file(ctx: RunContext, path: str, content: str) -> str:
    if path in PROTECTED_FILES and not ctx.tool_call_approved:
        raise ApprovalRequired
    return f'File {path!r} updated: {content!r}'

@agent.tool_plain(requires_approval=True)
def delete_file(path: str) -> str:
    return f'File {path!r} deleted'

result = agent.run_sync('Delete `__init__.py`, write `Hello, world!` to `README.md`, and clear `.env`')
messages = result.all_messages()

assert isinstance(result.output, DeferredToolRequests)
requests = result.output
print(requests)
"""
DeferredToolRequests(
    calls=[],
    approvals=[
        ToolCallPart(
            tool_name='update_file',
            args={'path': '.env', 'content': ''},
            tool_call_id='update_file_dotenv',
        ),
        ToolCallPart(
            tool_name='delete_file',
            args={'path': '__init__.py'},
            tool_call_id='delete_file',
        ),
    ],
)
"""

results = DeferredToolResults()
for call in requests.approvals:
    result = False
    if call.tool_name == 'update_file':
        # Approve all updates
        result = True
    elif call.tool_name == 'delete_file':
        # deny all deletes
        result = ToolDenied('Deleting files is not allowed')

    results.approvals[call.tool_call_id] = result

# The requested feature: pass a NEW user_prompt alongside deferred tool results,
# to steer the agent mid-flow rather than just approving/denying.
result = agent.run_sync(user_promp="continue", message_history=messages, deferred_tool_results=results)
"""
pydantic_ai.exceptions.UserError: Cannot provide a new user prompt when the message history contains unprocessed tool calls.
"""
```

Current behavior: pydantic-ai raises `UserError` when you try to pass a new `user_prompt` while message history still has unprocessed tool calls — the requester wants this relaxed/supported.

### References

*No response*

## Why this might matter to this vault

Relevant prior art for [[Proactive Customer Case Communicator]]'s Approve/Modify/Reject design: this issue is effectively asking for a third option beyond binary approve/deny — mid-flow steering via a new prompt. PCCC's "Modify" option already covers a similar need (the consultant edits the draft rather than just approving/rejecting it), so this is a useful cross-framework comparison point if PCCC's approval UX is ever revisited, but not something requiring any action now.
