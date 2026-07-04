---
title: "SLA won't be triggered due to undefined Contract"
aliases:
  - KB0864267
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864267
kb_number: KB0864267
last_modified: 2026-06-24
---

## SLA won't be triggered due to undefined Contract

  

### Issue

The contract value on case form is "undefined" when you populate contact on case form.

As a result the expected slas do not attach.

TO REPRODUCE:  
  
1\. Create New Case  
2\. Enter Contact. The Account will be filled automatically  
3\. Fill all other mandatory fields. Like Case Type and Short description.  
Result: The SLA won't be triggered. When looking at the XML-file the contract is 'undefined'.

### Release

N/A

### Cause

We have identified and found that the issue is because the 'Case display' rule BR has been customized.  
  
The Client script is designed to use the g\_scratchpad object and get the value from the BR for contract field.  
However as the BR is customized the g\_scratchpad object line related to contract has been commented, hence the Client script is not getting any value and passing undefined.  
  
  

### Resolution

Revert the OOB 'Case display' BR to the OOB upgrade version.  
/nav\_to.do?uri=sys\_script.do?sys\_id=71972922c312310087dcd02422d3ae9c  
  
Doing the above means the client script 'Populate contract and entitlement' can correctly load the Contract value on the form.  
  
After reverted the BR to OOB and cleared the cache and tested again. It started working as expected.  
  
1\. on the Case form the Contract is populated  
2\. In show xml there is no contract value  
3\. In Related list we see task slas attached.
