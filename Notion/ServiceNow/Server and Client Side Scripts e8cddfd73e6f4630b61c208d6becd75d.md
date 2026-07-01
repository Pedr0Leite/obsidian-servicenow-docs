---
aliases:
  - "Server and Client Side Scripts"
area: "Vault Root"
source: notion-export
tags:
  - script-include
  - client-script
  - business-rule
  - glide-record
  - scripting
---

# Server and Client Side Scripts

[How I made catalog client script onChange across a variable set](https://community.servicenow.com/community?id=community_question&sys_id=3534c729dbd8dbc01dcaf3231f96191d)

[Are Extension Points Worth It - GlideScriptedExtensionPoint](https://codecreative.io/blog/are-extension-points-worth-it/)

Extension Points are a very interesting feature when you create your own Custom Applications and you want to allow your customers / other developers to interject code into your application logic without breaking your own code.

For OOTB Script Include those Extension Points are hardly ever relevant because ServiceNow has close to no Extension Points built into their OOTB Script Includes.

With many OOTB Script Includes you find 2 versions: SNC and non-SNC

Never change SNC Script Includes, but always overwrite the non-SNC version.

This is actually intended to do like this by ServiceNow:

[https://docs.servicenow.com/bundle/sandiego-it-service-management/page/product/it-service-management/reference/customize-script-includes-itsm.html](https://docs.servicenow.com/bundle/sandiego-it-service-management/page/product/it-service-management/reference/customize-script-includes-itsm.html)

[Trigger Catalog Items from script](https://community.servicenow.com/community?id=community_question&sys_id=928a9f4ddb73ab805ed4a851ca961926)

[getXMLwait alternative for Service Portal](https://community.servicenow.com/community?id=community_article&sys_id=e37f2072db9fd0103daa1ea6689619c6)

onSubmit GlideAJax abort

```

function onSubmit() {
if (g_scratchpad.isFormValid){
	return true;
}
var actionName = g_form.getActionName();
var ga = new GlideAjax("SOMEFUNCTION");
ga.addParam(.....);
ga.getXML(function() {
	g_scratchpad.isFormValid = true;
	g_form.submit(actionName);
});
	return false;
}
```

[Script include Advance structure - Inheritance](Server%20and%20Client%20Side%20Scripts/Script%20include%20Advance%20structure%20-%20Inheritance%20addd1d50840e4665a67f1ef41389dd9e.md)

[CMDB - Change Parent Table](Server%20and%20Client%20Side%20Scripts/CMDB%20-%20Change%20Parent%20Table%2017ec42ce9a5680a0a337d311bf3ec803.md)

[Calculate Distance Between Two Locations in ServiceNow (without an API call!](Server%20and%20Client%20Side%20Scripts/Calculate%20Distance%20Between%20Two%20Locations%20in%20Servic%201c7c42ce9a56807daa3bc63eb7ff9c73.md)

[Possible Ways for Making an Attachment Mandatory : Service Portal/Native UI](Server%20and%20Client%20Side%20Scripts/Possible%20Ways%20for%20Making%20an%20Attachment%20Mandatory%20S%20293c42ce9a5680ee806bf2b83d7f063d.md)

[Scripted Extension Point](Server%20and%20Client%20Side%20Scripts/Scripted%20Extension%20Point%2030cc42ce9a568051b1c6c62664cb8367.md)

[Impersonate a user via script](Server%20and%20Client%20Side%20Scripts/Impersonate%20a%20user%20via%20script%20313c42ce9a5680828be3f959f6cb18d9.md)

[The Secrets of GlideDateTime](Server%20and%20Client%20Side%20Scripts/The%20Secrets%20of%20GlideDateTime%20357c42ce9a5680cfa38af0eb8bda8159.md)

## Related
- [[Calculate Distance Between Two Locations in Servic]]

- [[Script include Advance structure - Inheritance]]
- [[CMDB - Change Parent Table]]
- [[Impersonate a user via script]]
- [[Scripted Extension Point]]
- [[The Secrets of GlideDateTime]]
- [[Possible Ways for Making an Attachment Mandatory S]]