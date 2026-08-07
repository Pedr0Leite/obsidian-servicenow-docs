---
title: "Unable to create LDAP Server record - Blank screen OR Not authorized displayed on the screen."
aliases:
  - KB0724428
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724428
kb_number: KB0724428
last_modified: 2024-04-07
---

## Unable to create LDAP Server record - Blank screen OR Not authorized displayed on the screen.

  

### Issue

# Symptoms

* * *

Symptom 1: It says "Not authorized" when we click "Create New Server" OR  
Symptom 2: After filling the LDAP Server details, The screen goes white and does not do anything further after clicking "Submit".

When trying to create any new LDAP servers using below steps it fails to complete.

1) Go to "System LDAP" in Navigator  
  
2) "Create New Server" <---- Symptom 1 ("Not authorized" comes up on the screen)

![](sys_attachment.do?sys_id=e96a2466db42b450e515c22305961960)

  
3) If the above symptom is not seen, populate the fields as required for a new LDAP server. Click Submit.

4) Click "Submit" <---- Symptom 2 (Blank screen and nothing further happens)

![](sys_attachment.do?sys_id=ad6a2466db42b450e515c22305961965)

# Cause

* * *

OOTB Catalog Item/Record Producer (New LDAP Server) would be Inactive.

# Resolution

* * *

Navigate to the Record Producer table (sc\_cat\_item\_producer) and search for "New LDAP Server" in the name field. Activate the record.
