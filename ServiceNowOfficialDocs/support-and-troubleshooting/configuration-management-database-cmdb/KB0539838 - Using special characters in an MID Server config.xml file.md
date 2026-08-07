---
title: "Using special characters in an MID Server config.xml file"
aliases:
  - KB0539838
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0539838
kb_number: KB0539838
last_modified: 2025-10-16
---

## Using special characters in an MID Server config.xml file

  

### Issue

The XML specification defines five predefined entities that represent special characters and requires that all XML processors honor them. If these characters are used in a password, you will experience unexpected results. The most likely scenario to experience this conflict is when you set the password for a MID Server.

The following characters represent the five pre-defined entities:

-   "
-   &
-   '
-   <
-   \>

### XML and special characters

If you use the pre-defined entity characters in an XML file, such as the MID Server configuration file, you need to encode them.

To encode pre-defined entities into an XML document:

-   replace **"** with **&quot;**
-   replace **&** with **&amp;**
-   replace **'** with **&apos;**
-   replace **<** with **&lt;**
-   replace **\>** with **&gt;**

For example, to specify the password as **test&** in the MID Server config.xml file:

<parameter encrypt="true" name="mid.instance.password" value="test&amp;"/>
