---
title: "User field is not getting populated on the Software Subscriptions"
aliases:
  - KB2701492
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2701492
kb_number: KB2701492
last_modified: 2025-12-31
---

## User field is not getting populated on the Software Subscriptions

  

### Issue

User field is not getting populated on some or all of the Software Subscriptions.

### Release

Not release specific

### Cause

We try to find the matching sys\_user record for the samp\_sw\_subscription records using the below script:-  
https://<instance\_name>.service-now.com/sys\_script\_include.do?sys\_id=63dd30e187231300ec46ed4d87cb0b92  
  
getSysUser: function(input) {  
if (!gs.nil(input)) {  
var userResolutionUtil = new sn\_itam\_samp.SAMPUserResolutionUtil();  
var additionalQuery = userResolutionUtil.getQueryFromUserResolutionPolicy(input, 'saas');  
var upn = (typeof input === 'object') ? input.getValue('user\_principal\_name') : input;  
if (upn) {  
var query = 'email!=NULL^email=' + upn;  
query += '^NQuser\_name!=NULL^user\_name=' + upn.split('@')\[0\];  
if (additionalQuery) {  
query += '^NQ' + additionalQuery;  
}  
  
var userGr = new GlideRecord('sys\_user');  
userGr.addEncodedQuery(query);  
userGr.orderByDesc('active');  
userGr.setLimit(1);  
userGr.query();  
if (userGr.next()) {  
return userGr;  
}  
}  
}  
return null;  
}  
\------------------------------  
  
But if the above logic is unable to find matching sys\_user record for the integration then the User field will not be populated.

### Resolution

Customer need to configure valid resolution rules in 'samp\_user\_resolution\_rule' table based on their data to map the User field in the Software Subscription \[samp\_sw\_subscription\] table to an associated user in the User \[sys\_user\] table.

### Related Links

# [User resolution rule fields](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/reference/user-resolution-rule-fields.html)
