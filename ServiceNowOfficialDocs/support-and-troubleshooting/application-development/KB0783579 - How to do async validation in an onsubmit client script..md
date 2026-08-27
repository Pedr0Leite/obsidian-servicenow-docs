---
title: "How to do async validation in an onsubmit client script."
aliases:
  - KB0783579
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783579
kb_number: KB0783579
last_modified: 2025-01-22
---

## How to do async validation in an onsubmit client script.

  

### Summary

The GlideAjax (Asynchronous) does not work on onSubmit Client Script. This is because of the fundamental behavior of Asynchronous scripts which are non-blocking by nature.

### Release

All Versions

### Instructions

To mitigate this fundamental behavior, the form should be submitted again and this should be handled in the callback function of the getXML.

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
