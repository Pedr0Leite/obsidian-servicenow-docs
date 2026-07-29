---
title: "If OAuth application registry authorization URL contains extra query parameter then URL is formatting wrongly and throwing 404 error"
aliases:
  - KB0786459
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786459
kb_number: KB0786459
last_modified: 2024-04-26
---

## If OAuth application registry authorization URL contains extra query parameter then URL is formatting wrongly and throwing 404 error

  

### Issue

If OAuth application registry authorization URL contains extra query parameter then URL is formatting wrongly with extra "?" mark in URL and throwing an error as 404 after we click on Get OAuth token in REST message  if you see the URL in the screenshot we can observer "?" mark after Authorize and after Service\_now, here p=B2C\_1\_Service\_now is extra query parameter in Authorization URL

### Release

All

### Cause

For example, your Authorization URL contains an extra query parameter as shown here "_**https://URL.domain.com/oauth2/v2.0/token?p=B2C\_1\_Service\_Now**_" and when you click on Get OAuth Token in REST message request URL will get generated with extra "?" mark back to back which causes URL as invalid and throws 404 error as below, if you see the URL in the screenshot we can observer "?" mark after Authorize and after Service\_now, here p=B2C\_1\_Service\_now is extra query parameter in Authorization URL

![](sys_attachment.do?sys_id=76ed96cddbd508544819fb24399619cd)

### Resolution

-   In order to resolve this issue, we need to remove that extra query parameter from Authorization URL and override by creating one script include which extends the OOB OAuthUtil script include as below.

_**var OAuthUtil1 = Class.create();
OAuthUtil1.prototype = Object.extendsObject(OAuthUtil, {
    preprocessAuthCode: function(requestParamMap) {
        requestParamMap.put("p", "B2C\_1\_Service\_Now");
    },

	postprocessAccessToken: function(accessTokenResponse) {
        
        var contentType = accessTokenResponse.getContentType();
		if (contentType && contentType.indexOf('application/json') != -1) {
			var tokenResponse = (new global.JSON()).decode(accessTokenResponse.getBody());
			var paramMap = accessTokenResponse.getparameters();
			for (param in tokenResponse) {
				if (param == 'id\_token') {
					paramMap.put("access\_token", tokenResponse\[param\].toString());
				}
				else {
					paramMap.put(param, tokenResponse\[param\].toString());
				}
            }
		}
    },

    type: 'OAuthUtil1'
});  
  
  
**_\*Once the script is created then we can refer this custom script on OAuth API script field which will be available in that particular application registry
