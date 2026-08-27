---
title: "CMDB Identification Error: Missing mandatory field"
aliases:
  - KB0723079
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723079
kb_number: KB0723079
last_modified: 2025-05-08
---

## CMDB Identification Error: Missing mandatory field

  

### Issue

IRE Identification operation fails with Mandatory field error.

CMDB Identification Error: Missing mandatory field

or something more specific like:

Discovery error 'Identifier: validation error: cmdb\_ci\_ip\_address: missing mandatory fields: name'

### Release

All recent releases. More likely to be seen after Probe to Pattern migration for Discovery.

### Cause

You will encounter this issue when the system property "glide.required.attribute.enabled" is set to "true", and the CMDB Identification & Reconciliation engine looks for all the mandatory attributes for a particular CI class/Table, as set in the Dictionary or CI Class Manager, and checks to see if all the mandatory values are coming in as part of the payload. 

e.g. If "location" is set as Mandatory on the cmdb\_ci\_win\_server class, Identification engine expects it to be part of the payload before it tries to insert/update into the table.

### Resolution

There are at least 3 ways to avoid this error:

-   **Include the field value in the IRE Payload**. That may not be possible if the update is being done by OOTB code, that you have no control over, designed not to include this field.
-   **Set system property glide.required.attribute.enabled=false**, in table sys\_properties. We already have required attributes as part of identifiers that are used for identification and reconciliation. Having Mandatory attributes on the class that are not brought in by discovery at Identification will now not result in the error.
-   **Decide if the field really does need to be set as Mandatory** in the Dictionary, and set it false/not-mandatory instead. If this was a customisation, to prevent users submitting CI forms without the value, **perhaps using a UI Policy or Client Script would be a better alternative**.
