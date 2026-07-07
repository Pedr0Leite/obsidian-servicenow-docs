---
title: "The field sn_vul_vulnerabilities.filter_type is not visible on the Vulnerabilities form"
aliases:
  - KB0727007
tags:
  - servicenow
  - support-kb
  - vulnerability-response
  - client-scripts
  - form-fields
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727007
kb_number: KB0727007
last_modified: 2024-04-07
---

## The field sn\_vul\_vulnerabilities.filter\_type is not visible on the Vulnerabilities form

  

### Issue

* * *

On the sn\_vul\_vulnerability form, the filter\_type field is visible only for a fraction of a second when the page loads. 

  

### Release

London (after upgrade from previous releases such as Jakarta) 

Vulnerabilities (sn\_vul\_vulnerabilities) is part of a special plugin, [Vulnerability Response](https://empgmorales2.service-now.com/v_plugin.do?sys_id=com.snc.vulnerability&sysparm_record_target=v_plugin&sysparm_record_row=4&sysparm_record_rows=6&sysparm_record_list=nameCONTAINSvulne%5EORDERBYname).

#   

### Cause

There is a OOB client script that hides this field whenever the value of that field is equal to 'Group Value'.  The name of the client script is 'Handle filter type changes'

\>>> https://\[INSTANCE-NAME\].service-now.com/nav\_to.do?uri=sys\_script\_client.do?sys\_id=3cc5af88e741130068c32b63c2f6a9c1

Note that this particular client script is designed to run onChange and onLoad, despite its official onChange status. 

### Resolution

This is default OOB behavior which can be customized to allow the field to be visible under any number of circumstances. 

### Related Links

More info on the Vulnerability Response plugin and its applications can be found at [https://docs.servicenow.com/csh?topicname=vuln-landing-page.html&version=latest](https://docs.servicenow.com/csh?topicname=vuln-landing-page.html&version=latest)

## Related

- [[KB0727840 - Tenable Integeration for Vulnerability Response does not honor 'CI Classes to Ignore' correctly]] - other Vulnerability Response troubleshooting
- [[KB0725789 - Mid server alerts are being sent to the users who has sn_vul_r7.admin role, since it contains 'mid_server' role.]] - Vulnerability Response role/plugin behavior

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
