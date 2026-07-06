---
title: "OAuth token helper"
aliases:
  - OAuth token helper
tags:
  - servicenow-dev-program
  - code-snippet
  - oauth-token-helper
  - script-includes
---

# Helps to get Refresh Token based on username and password or get the Access Token based on the Refresh Token
# To be noted that this is using the new ES2021 feature. So if your instance is upgraded to Xanadu or you are using a Scoped App that already enabled the ES2021 then this Script Include can be used.

# Example

```
var helper = new OAuthTokenHelper();

var result = helper.getRefreshAndAccessTokens("oauth_profile_id", "context e.g. Sales", "user@service-now.com", "username", "password") 

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
