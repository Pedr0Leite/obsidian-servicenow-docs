---
title: "How to resolve CI reclassification errors during discovery"
aliases:
  - KB0812249
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812249
kb_number: KB0812249
last_modified: 2026-04-01
---

## How to resolve CI reclassification errors during discovery

  

### Issue

During discovery of configuration items (CI), you may see an error that says "CI Reclassification not allowed". For example: 

CI Reclassification not allowed from class: \[cmdb\_ci\_msd\] to \[cmdb\_ci\_storage\_node\_element\]

### Release

All supported releases

### Cause

This error occurs when the Identification and Reconciliation Engine (IRE) attempts to reclassify a CI from one class to another, but the system does not allow reclassification based on current settings.

You can upgrade, downgrade, or switch the class of a CI by modifying its class attribute. During the CI identification process, a CI might need to be reclassified to a different sys\_class\_name type. 

By default, CIs are reclassified automatically. If automatic reclassification is disabled, the CI is not reclassified and the system generates a reclassification task for your review.

### Resolution

To avoid this error, you can adjust system properties, IRE payload flags, and the payload.

#### System properties

The following system properties control if a class upgrade, downgrade, or switch are allowed:

-   glide.class.upgrade.enabled
-   glide.class.downgrade.enabled
-   glide.class.switch.enabled
-   glide.identification\_engine.update\_without\_switch\_enabled
-   glide.identification\_engine.update\_without\_downgrade\_enabled
-   glide.identification\_engine.update\_without\_upgrade\_enabled

#### Payload flags and adjusting payload

1.  Go to **Configuration** \> **Identification/Reconciliation** > **Reclassification**.
2.  Review the payload.
3.  Adjust the payload to avoid reclassification, if possible.   
    -   This is possible for some of the applications that call the IRE. For example, transforms can run scripts to adjust the payload.
4.  You can temporarily override the IRE reclassification properties at the payload item level using the following flags: 

-   -   classUpgrade
    -   classDowngrade
    -   classSwitch

**Note**: If either of these payload setting flags is set to true, it overrides the relevant property (for example, glide.class.upgrade.enabled). 

Add the following flags under the items.settings object to explicitly control reclassification behavior:

{ items: \[{className: "cmdb\_ci\_server", classUpgrade: true, classDowngrade: true, classSwitch: true, values: {name: "linux123", serial\_number: "12srt567"...

-   updateWithoutUpgrade
-   updateWithoutDowngrade
-   updateWithoutSwitch

**Note:** These settings work in conjunction with the related system properties. If _either_ the payload flag or the system property is **true**, the system updates the CI without changing its class. 

Add the following flags under the items.settings object to explicitly control update behavior without class change:

{ items: \[{className: 'cmdb\_ci\_server',values: {name: 'linux123'},"settings": {"skipReclassificationRestrictionRules" : "true", "updateWithoutSwitch": "false"}...

  
**Important notes**

Updating the payload before it is sent to the IRE is specific to the application which is passing data to the IRE.

Modifications can be applied via:

-   Transform scripts (for data imports)
-   Pre/post-processing scripts (for Discovery)
-   Custom integrations

### Related Links

-   [Reclassify a CI](https://www.servicenow.com/docs/csh?topicname=t_ManuallyReclassifyCI.html&version=latest "Reclassify a CI")
-   [Configure CI reclassification during IRE processing](https://www.servicenow.com/docs/csh?topicname=c_CIReclassification.html&version=latest) 
-   [Properties for Identification and Reconciliation](https://docs.servicenow.com/csh?topicname=properties-id-reconciliation.html&version=latest "Properties for Identification and Reconciliation")
