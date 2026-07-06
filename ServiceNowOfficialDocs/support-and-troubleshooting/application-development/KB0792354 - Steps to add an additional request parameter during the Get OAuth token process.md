---
title: "Steps to add an additional request parameter during the Get OAuth token process"
aliases:
  - KB0792354
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792354
kb_number: KB0792354
last_modified: 2024-03-04
---

## Steps to add an additional request parameter during the Get OAuth token process

  

### Issue

Some OAuth providers require additional parameters to be included beyond those already added by ServiceNow from the OAuth entity profile.  
  
Additional parameters can be added by customizing the OAuthUtil script include. Please refrain from editing the out-of-the-box OAuthUtil script include. Instead, you can extend the out-of-the-box 'OAuthUtil' script include and add the custom parameters by referring to the sample script provided below.

### Release

All

### Resolution

We typically require "Client ID," "Client Secret," "Grant Type," and "Token URL," but some OAuth providers may necessitate an additional parameter such as "resource" or "audience". 

Currently, it is not feasible to pass these extra parameters from the UI. As a result, we request customers to follow the below steps.

Step 1: Extend the out of the box 'OAuthUtil' script include and add the custom parameters by following the below sample script.

```
interceptRequestParameters: function(requestParamMap) {
		// Add/Modify request parameters if needed
		requestParamMap.put('resource','https://xxxx.core.yyy.net/');
		this.preprocessAccessToken(requestParamMap);
	},
```

Step 2: In the OAuth Application Registry make sure to update the "OAuth API Script" field to point to the script include created in Step 1.
