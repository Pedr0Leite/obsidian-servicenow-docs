---
title: "multi-row variable sets will be displayed in random order in variable editor when submitted with sn_sc.CartJS."
aliases:
  - KB0753493
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753493
kb_number: KB0753493
last_modified: 2024-04-07
---

## multi-row variable sets will be displayed in random order in variable editor when submitted with sn\_sc.CartJS.

  

### Issue

# Symptoms

When use script to order record producers with multi-row variable sets, the generated record has unexpected variables displayed in the variable editor in random order.

Steps to reproduce:

1\. Create a multi-row variable set with a few variables in it. 

2\. Make sure the record producer table has variable editor configured as per the following DOC:   
[https://docs.servicenow.com/csh?topicname=configure-default-variable-editor.html&version=latest](https://docs.servicenow.com/csh?topicname=configure-default-variable-editor.html&version=latest) 

3\.  "Try it" the Record Producer in service catalog.

(Leave the multi-row variables blank.) 

4\. Review the submitted incident, the variable display is all correct. 

5\. Now, run the followin script to order the record producer. 

var cartOne = new sn\_sc.CartJS(); 

var requestInc = 

{ 

'sysparm\_id': '3f1dd0320a0a0b99000a53f7604a2ef9', 

'variables':{ 

'urgency': '1', 

'comments': 'SNC test INT', 

} 

}; 

var cartDetailsOne = cartOne.orderNow(requestInc); 

6\. Review the submitted incident, the variable display is unexpected. 

# Release

Madrid

# Cause

This is due to using the wrong API for a record producer.

# Resolution

Use below API instead:

var record = new sn\_sc.CatItem('3f1dd0320a0a0b99000a53f7604a2ef9');   
var requestInc =   
{   
'sysparm\_id': '3f1dd0320a0a0b99000a53f7604a2ef9',   
'variables':{   
'urgency': '1',   
'comments': 'SNC test INT',   
}   
};   
var recordDetails = record.submitProducer(requestInc);
