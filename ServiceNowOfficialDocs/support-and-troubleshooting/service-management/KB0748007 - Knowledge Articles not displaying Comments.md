---
title: "Knowledge Articles not displaying Comments "
aliases:
  - KB0748007
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748007
kb_number: KB0748007
last_modified: 2024-04-07
---

## Knowledge Articles not displaying Comments

  

### Issue

The customer experienced that none of their Knowledge Articles are displaying Comments.

### Release

London Patch 6

### Cause

UI Macro 'kb\_view\_common\_footer' is not active.

While debugging we found the error below in the Debug output

14:17:30.700: /glide/nodes/xxxxxxxxxx/webapps/glide/itil/WEB-INF/ui.jtemplates/kb\_view\_common\_footer (No such file or directory): no thrown error  
  
log14:17:30.701: running script: kb\_view\_common\_footer the following error occurred: no thrown error  
  
log14:17:30.703: null:-1:-1: <null> No source to compile: file:/glide/nodes/xxxxxxxxxx/webapps/glide/itil/WEB-INF/ui.jtemplates/kb\_view\_common\_footer: org.apache.commons.jelly.JellyException: null:-1:-1: <null> No source to compile: file:/glide/nodes/xxxxxxxxxx/webapps/glide/itil/WEB-INF/ui.jtemplates/kb\_view\_common\_footer: com.glide.ui.jelly.GlideJellyContext.compileIGlideTemplateXML(GlideJellyContext.java:845) com.glide.ui.jelly.GlideJellyContext.runScript(GlideJellyContext.java:773) com.glide.ui.jelly.tags.BaseTag.invokeNoRef(BaseTag.java:100) com.glide.ui.jelly.tags.BaseTag.invoker(BaseTag.java:87) com.glide.ui.jelly.tags.form.InlineTag.doTag(InlineTag.java:46) org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)

Upon investigating we identified that the UI Macro 'kb\_view\_common\_footer' has been made inactive:

https://xxxxxxxx.service-now.com/nav\_to.do?uri=sys\_ui\_macro.do?sys\_id=a9240ca0d72321004792a1737e6103c9

The script in the above file on line 102 references the relevant Macro below which should display the comments section

<g:inline template="kb\_article\_comments" />

### Resolution

Reactivate the UI Macro 'kb\_view\_common\_footer':

https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_ui\_macro.do?sys\_id=a9240ca0d72321004792a1737e6103c9
