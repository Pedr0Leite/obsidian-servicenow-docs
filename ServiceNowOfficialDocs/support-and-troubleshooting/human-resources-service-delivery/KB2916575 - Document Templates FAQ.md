---
title: "Document Templates FAQ"
aliases:
  - KB2916575
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2916575
kb_number: KB2916575
last_modified: 2026-06-30
---

## Text

 

## Overview

Using Document Templates application (sn\_doc), you can create HTML and PDF document templates to generate or sign the documents.

## Frequently Asked Questions

### Why can the user sign the document but not edit any fields in an editable PDF document template?

This happens when the participant is missing or not assigned for the editable fields in the PDF document template. Field edit access is controlled by participant mapping in Template Mappings.

-   Go to PDF document template -> Template Mappings (Related List)
-   For each field that needs to be edited, ensure that participant is set in Template Mapping record.

### Does ServiceNow Document Templates application provide an audit trail signed documents out of the box?

No. ServiceNow Document Templates application does not support audit trails.

### What value should a template mapping script return for a checkbox field when filling a PDF form?

-   Standalone checkbox: Return any non-"Off" string (e.g. "On") to check it, or "Off" to uncheck it. The system auto-resolves the correct on-state.
-   Grouped checkbox (with kids): Return the exact option name as defined in the PDF form for that checkbox (e.g. "Option1", "Choice\_A") to check that option, or "Off" to uncheck all.

### Why are some HTML tags and attributes being stripped from my HTML document templates after the upgrade when previewing/pdf generation?

HTML sanitization was introduced for security purposes as part of [PRB2023551](/problem.do?sys_id=517232b9477c8f50c1b46d0a636d4340). The sanitizer removes HTML elements, tags, and attributes not on the built-in allowlist. Check _[Exploring HTML sanitizer](https://www.servicenow.com/docs/r/platform-security/exploring-html-sanitizer.html)_ for built-in inclusion list. See [Configuring the HTML Sanitizer](https://www.servicenow.com/docs/r/platform-security/t_ConfigureHTMLSanitizer.html) for allowlist configuration.

The "Sanitize" boolean field on HTML document template table controls this sanitization behavior. This field is set to false on existing templates but set to true on all new templates. When sanitization is enabled, you see the message "The output of this HTML template is sanitized. Unsupported or unsafe HTML will be removed." under the body field on form. The _sanitize_ field is hidden by default on form. _sn\_doc.admin_ users can see this field by clicking Advanced View in Related Links. Recommend to set this field to true to secure all your templates.

 Docs: [Configure an HTML document template](https://www.servicenow.com/docs/r/employee-service-management/hr-service-delivery/configure-HTML-doc-template.html?content-lang=en-US)

## Additional Information

-   [Document Templates Docs](https://www.servicenow.com/docs/r/employee-service-management/hr-service-delivery/document-templates-overview.html)
-   [HR Document Templates to Document Templates migration FAQ](/kb?id=kb_article_view&sysparm_article=KB2919559)
