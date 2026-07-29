---
title: "Smart Incident Categorizer AI"
aliases:
  - Smart Incident Categorizer AI
tags:
  - servicenow-dev-program
  - code-snippet
  - smart-incident-categorizer-ai
  - restmessagev2
---

# Smart Incident Categorizer using AI

## Description
Automatically categorizes incidents using OpenAI GPT-3.5 based on description content.

## Use Case
- Auto-assigns category when incidents are created without category
- Reduces manual categorization effort
- Improves consistency in incident classification

## Setup
1. Create system property: `openai.api.key` with your OpenAI API key
2. Create Business Rule on `incident` table
3. Set to run `before insert` when category is empty

## Categories
Returns one of: network, hardware, software, database, security, email

## Testing
Create incident without category - verify auto-assignment in work notes.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/API for Automatic Group creation/README|API for Automatic Group creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Auth2 client credentials token cache with auto-refresh/README|Auth2 client credentials token cache with auto-refresh]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
