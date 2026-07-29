---
title: "Single Sign On Logout is taking 2 clicks on the Logout button to logout from instance."
aliases:
  - KB0686259
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686259
kb_number: KB0686259
last_modified: 2024-04-07
---

## Issue

# Issue Overview

* * *

Single Sign On Logout is taking 2 clicks on the Logout button to logout from instance.

# Symptoms

* * *

1) The first click on the logout button takes to a window with a warning 'This content cannot be displayed in a frame'

![](sys_attachment.do?sys_id=e41d2462db82b450e515c22305961995)

2) OR a Blank page.

![](sys_attachment.do?sys_id=601d2462db82b450e515c2230596199b)

# Troubleshooting

* * *

1) Confirm if any IDP Logout URL is configured on the Identity Provider record.

2) Set the following on the Identity Provider record configuration to see if ServiceNow logout works :

**External logout redirect** field to **external\_logout\_complete.do** or Empty out the field.

![](sys_attachment.do?sys_id=a81d2462db82b450e515c223059619a0)

**Protocol Binding for the IDP's SingleLogoutRequest** field to **urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST**

**![](sys_attachment.do?sys_id=e01d2462db82b450e515c223059619a6)**

 3) After setting the above fields on the IDP record, click on Logout button on the instance ONCE and see that the following page comes up. This means that ServiceNow session was successfully terminated.

![](sys_attachment.do?sys_id=2c1d2462db82b450e515c223059619ab) 

# Cause/Solution

* * *

-   Either **SAML Logout Response** is not coming to the ServiceNow instance from IDP for the **SAML Logout Request** sent to the IDP from ServiceNow, when the Logout happens for SSO authenticated session.  
      
    You can confirm both **SAML Logout Request/Response** in the Script Log Statements once the Multi SSO debug is enabled.  
    Multi-Provider SSO > Administration > Properties > **CHECK** Enable multiple provider SSO
-   Or the **External logout redirect** URL populated in the IDP record is incorrect.

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="text-align: center;" width="25"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="text-align: left;"><strong>Note</strong>: In both, the cases customer will need to reach out to their IDP admin to look into the issue as the issue doesn't happen when ServiceNow default&nbsp;External logout redirect URL is set.</td></tr></tbody></table>
