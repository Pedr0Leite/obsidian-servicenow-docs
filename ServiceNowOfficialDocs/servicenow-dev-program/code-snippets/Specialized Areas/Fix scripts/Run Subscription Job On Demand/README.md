---
title: "Run Subscription Job On Demand"
aliases:
  - Run Subscription Job On Demand
tags:
  - servicenow-dev-program
  - code-snippet
  - run-subscription-job-on-demand
  - fix-scripts
---

# Usage
If you wish to update/re-calculate your allocated entitlements on the subscription management dashboard, execute the following two lines of code. You can run this server script either in the background script or maintain it as a fix script and run it on-demand.

```
var summarizer = new SNC.SubscriptionSummarizer();
		             summarizer.runSummary();
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
