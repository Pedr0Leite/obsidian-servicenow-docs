---
title: "Extension Sections are failing to execute in a Pattern"
aliases:
  - KB0693347
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693347
kb_number: KB0693347
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

-   You have created some extension sections on a pattern but they do not seem to be triggering at all.
-   Extension sections will run right after the Identification (ID) section.
-   When you look at the pattern log, you will see the ID section run and then nothing below it.
-   If you see an extension section there but the icon next to it is red/yellow/green then this KB will not address the issue you have
-   If you DO NOT see the extension section at all on the pattern log but you know its there on the pattern then this KB will address that issue.
-   You will also see error messages in the MID server logs that looks like the following:
    -   Worker-Expedited:ServiceDiscoveryProbe WARNING \*\*\* WARNING \*\*\* (87)ReferenceLibraryFactory - Failed to find library by ID: _\[sys\_id of the extension section pattern record\]_. will try by name&#13;  
        07/19/18 16:10:09 (861) Worker-Expedited:ServiceDiscoveryProbe WARNING \*\*\* WARNING \*\*\* (87)PatternExtensionsExecutor - Failed to prepare extensions list due to: Library not found, id: f0927228dbda1b80a628a3cc0b9619ac&#13;
    -   Worker-Expedited:ServiceDiscoveryProbe WARNING \*\*\* WARNING \*\*\* org.mozilla.javascript.EcmaError: Cannot convert null to an object.  
        Caused by an error in Ad-hoc script 'EvalClosure-clean \[_some field name_\]' at line _x_

# Release

* * *

-   Any that use patterns

# Cause

* * *

-   The cause for this is because of the of the extension section that you have under that pattern is set to Active = False.
-   If you have multiple extension sections, even if one of them is not active NONE of them will be attempted during your discovery or service mapping.

# Resolution

* * *

-   Make all used extension section patterns Active = True
-   If there is one extension section that is included in a pattern but you do not want it active, then it needs to be removed from the pattern it is currently assigned to
