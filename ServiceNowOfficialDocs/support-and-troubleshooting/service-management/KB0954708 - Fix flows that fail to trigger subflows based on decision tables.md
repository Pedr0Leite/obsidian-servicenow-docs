---
title: "Fix flows that fail to trigger subflows based on decision tables"
aliases:
  - KB0954708
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954708
kb_number: KB0954708
last_modified: 2026-02-11
---

## Fix flows that fail to trigger subflows based on decision tables

  

### Issue

If a flow fails to trigger a subflow when using a decision table, you may see these errors in the logs: 

"WARNING \*\*\* WARNING \*\*\* Get for non-existent record: sys\_hub\_flow:, initializing"

"Executing flow: (sys\_flow\_context sys\_id: <sys\_id>)"

"WARNING \*\*\* WARNING \*\*\* Error registering filter: : Query String cannot be empty"

### Release

Any supported release

### Cause

This issue occurs when:

-   The condition input does not match any entry in the decision table.
-   The condition in the decision table is blank.

### Resolution

1\. Verify if the issue is related to the decision table.

2\. If the response is null, this indicates the decision table isn't matching any inputs passed by the flow.

3\. To check the decision table, run this API script:

var dt = new sn\_dt.DecisionTableAPI();  
var inputs = new Object();  
inputs\[‘flow\_input\_variable\_name’\] = 'flow\_input\_variable\_value';  
var response = dt.getDecision('decision\_table\_sys\_id', inputs);  
gs.print(response);

4\. Check the condition of your expected decision record, and then populate it to exactly match the flow inputs. 

**Note**: Blank conditions will not match any flow evaluation using either **First decision that matches** or **Run all decisions that match** options. 

### Related Links

[Make a decision flow logic](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/administer/flow-designer/concept/flow-logic-make-decision.html "Make a decision flow logic")
