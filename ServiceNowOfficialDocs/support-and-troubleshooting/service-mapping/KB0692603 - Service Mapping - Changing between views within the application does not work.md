---
title: "Service Mapping - Changing between views within the application does not work"
aliases:
  - KB0692603
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692603
kb_number: KB0692603
last_modified: 2024-04-07
---

## Service Mapping - Changing between views within the application does not work

  

### Issue

# Symptoms

* * *

When viewing a Service within the Service Mapping application, switching between form views does not work. The form appears to reload but you are still redirected to the same view.

![](/sys_attachment.do?sys_id=7d89a422db42b450e515c22305961971)

# Release

* * *

All

# Cause

* * *

The Service Mapping application uses the GET parameter "sysparm\_userpref.cmdb\_ci\_service\_discovered=<view\_name>" in the URL it redirects to when switching between the different views of a form.

`https://<instance-name>.service-now.com/incident.do?sys_id=85071a1347c12200e0ef563dbb9a71c1&sysparm_userpref.cmdb_ci_services_discovered.view=questionnaire`

What this does is it changes your user preference "cmdb\_ci\_service\_discovered" to the view name specified. Then, the system will open the form and look to the user preference that's just been stored to determine which view the form should be in. However, the GET parameter is being ignored.

This is due to the system property "glide.ui.remember\_view" being set to false. This property controls the default behavior of being redirected to the view stored in the user preference for your profile when visiting a List or Form that you've been on before. With the property set to false, the expected behavior is for the system to redirect users to the default view defined for a form rather then the one stored in the user preference.

# Resolution

* * *

Change the system property 'glide.ui.remember\_view' to true.

![](/sys_attachment.do?sys_id=bd89a422db42b450e515c22305961976)
