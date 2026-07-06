---
title: "Pattern errors when creating connection using Inclusion Endpoint"
aliases:
  - KB0716333
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716333
kb_number: KB0716333
last_modified: 2023-07-12
---

## Pattern errors when creating connection using Inclusion Endpoint

  

### Issue

# Symptoms

* * *

Custom pattern is created, in its connection section, last step is an inclusion connection type to another entry point, however upon creating this connection step and saving the pattern, similar error is displayed:

**Invalid ndl, NotSystemErrorEntry point type <inclusion endpoint CI type> in step <step name> in connection section <section name> is not defined on any pattern of relevant included CI.**

  

and/or the error below:

  
**Invalid ndl, NotSystemErrorEntry point type <inclusion endpoint CI type> in step <step name> in connection section <section name> does not match any containment rule.**

# Release

* * *

Any 

# Cause

* * *

For the error below:

**Invalid ndl, NotSystemErrorEntry point type <inclusion endpoint CI type> in step <step name> in connection section <section name> is not defined on any pattern of relevant included CI.**

This error means that no pattern is defined that contains an identification section with the CI type specified in the inclusion. By taking as example the out-of-the-box Jboss pattern, the inclusion connection is tied to the entry point type "Jboss Module inclusion" which is the entry point type of the identification section of the Jboss module pattern.

![](/sys_attachment.do?sys_id=dc1ffce2db0ab450e515c2230596194b)

  

The error below means that a containment rule is not properly configured:

**Invalid ndl, NotSystemErrorEntry point type <inclusion endpoint CI type> in step <step name> in connection section <section name> does not match any containment rule.**

Using Jboss pattern as example, we notice that there is a containment rule "_JBoss Contains Jboss module_", so if you are creating a custom pattern with inclusion connections, make sure that appropriate containment rules are created.

![](/sys_attachment.do?sys_id=501ffce2db0ab450e515c22305961951)

# Resolution

* * *

-   Create **containment rules** in the Metadata Editor
-   Make sure there is a pattern with same entry point type as defined in the inclusion connection step of your custom pattern.
