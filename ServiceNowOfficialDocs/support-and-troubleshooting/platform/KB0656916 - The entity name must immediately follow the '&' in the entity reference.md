---
title: "The entity name must immediately follow the '&' in the entity reference"
aliases:
  - KB0656916
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656916
kb_number: KB0656916
last_modified: 2024-12-12
---

## The entity name must immediately follow the '&' in the entity reference

  

### Issue

This issue occurs when a web application processes data containing special characters like the ampersand (`&`) but does not properly encode it before displaying it in an HTML interface. 

-   When an application processes and displays data, it might include the ampersand (`&`) character.
-   In HTML, `&` is a reserved character used to start an entity reference (ex., `&amp;` represents `&`).
-   If the application fails to encode `&` properly (ex., as `&amp;`), the HTML parser expects a valid entity name to follow it.

### Symptoms

Some applications fail and the error displayed is: **The entity name must immediately follow the (`&`) in the entity reference.**

### Release

All Releases

### Cause

The web applications internally work with the data. On certain conditions, the data could interfere with the interface rendering the data itself. On this case, the data that contains and (`&`) that is not translated to the equivalent web escaped code, and it could breaks the user interface HTML.

-   The application is working with raw data containing `&` without translating it to `&amp;`.

### Resolution

Make sure the following system properties are set to **true** in your instance:

-   glide.ui.escape\_all\_script
-   glide.ui.escape\_text

### Related Links

Documentation:

[Escape XML (instance security hardening)](https://www.servicenow.com/docs/csh?topicname=escape-xml.html&version=latest "Escape XML (instance security hardening)")

[Escape jelly script \[Updated in Security Center 1.3 and 1.5\]](https://www.servicenow.com/docs/csh?topicname=sc-escape-jelly.html&version=latest "Escape jelly script [Updated in Security Center 1.3 and 1.5]")

Knowledge:

[Troubleshooting error "Entity name must immediately follow <character> in the entity reference"](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0517446 "Troubleshooting error \"Entity name must immediately follow <character> in the entity reference\"")

Community:

[The entity name must immediately follow the '&' in the entity reference](https://www.servicenow.com/community/developer-forum/the-entity-name-must-immediately-follow-the-amp-in-the-entity/m-p/2573906 "The entity name must immediately follow the '&' in the entity reference")
