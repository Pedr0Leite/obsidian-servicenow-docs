---
title: "When Enterprise level Agreement Type is selected the product is showing as compliant"
aliases:
  - KB1709855
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1709855
kb_number: KB1709855
last_modified: 2026-03-27
---

## When Enterprise level Agreement Type is selected the product is showing as compliant

  

### Summary

1.  This is expected behaviour OOTB. When an Enterprise-level Agreement is selected, it will not affect the compliance.  
        Affects Compliance value is calculated based on the below script.
2.  https://<instancename>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=3ed4099053900010d924ddeeff7b12ec
    -     
        } else {  
        var remediationOption = new GlideRecord(ReconciliationConstants.REMEDIATION\_OPTION\_TABLE);  
        remediationOption.addQuery('software\_model\_result', softwareModelResult);  
        remediationOption.addQuery('remediation\_action', ReconciliationConstants.REMOVE\_UNLICENSED\_CLOUD\_INSTALLS);  
        remediationOption.query();  
        if (remediationOption.next()) {  
        remediationOption.setValue('unlicensed\_rights', remediationOption.getValue('rights\_needed'));  
        remediationOption.setValue('actionable\_rights', remediationOption.getValue('rights\_needed'));  
        remediationOption.setValue('affects\_compliance', !this.softwareModelsWithELA.hasOwnProperty(softwareModel));  
        remediationOption.setValue('true\_up\_cost', 0);  
        remediationOption.update();  
        }
3.  The softwareModelsWithELA, which is a software model with an Enterprise Licence Agreement.

Note: This applies only when you have entitlements matching data in the software installs and subscriptions table's
