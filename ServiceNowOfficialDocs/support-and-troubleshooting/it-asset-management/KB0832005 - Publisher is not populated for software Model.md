---
title: "Publisher is not populated for software Model"
aliases:
  - KB0832005
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832005
kb_number: KB0832005
last_modified: 2024-12-17
---

## Issue

1.  Software Discovery Models contain (empty) Publisher entries.
2.  For example filter with display name starts with 'Microsoft'.  
      
    ![](sys_attachment.do?sys_id=79d27085db40b4d0b55f0b55ca96190c)  
      
    
3.  Manufacturer will be empty for Software Publisher 'Microsoft'.  
      
    ![](sys_attachment.do?sys_id=f1d27085db40b4d0b55f0b55ca96190b)  
    

## Resolution

1.  Updating the publishers to point existing core company records where name was not empty and normalized column value = true via running below script from background scripts.  
      
    
    <table style="border-collapse: collapse; width: 49.7004%; height: 439px;" border="1"><tbody><tr style="height: 403px;"><td style="width: 100%; height: 403px;">var publlisherToCoreCompany = {};<br><br>publlisherToCoreCompany['Adobe Systems'] = '10920286db0d1c10888bd054d496190f';<br>publlisherToCoreCompany['Citrix Systems'] = 'e0920286db0d1c10888bd054d496196b';<br>publlisherToCoreCompany['IBM'] = '2b70af9bdb991090bcdb6c391396190b';<br>publlisherToCoreCompany['Oracle'] = '18920286db0d1c10888bd054d4961913';<br>publlisherToCoreCompany['VMware, Inc.'] = 'f2728e86dbcddc101309e3a84b9619fc';<br>publlisherToCoreCompany['Microsoft'] = '5892ce46db0d1c10888bd054d49619d3';<br><br>Object.keys(publlisherToCoreCompany).forEach(function(key){<br><br>&nbsp;var grPublisher = new GlideRecord('samp_sw_publisher');<br>&nbsp;grPublisher.addQuery('name', key);<br>&nbsp;grPublisher.addNotNullQuery('manufacturer');<br>&nbsp;grPublisher.addNullQuery('manufacturer.name');<br>&nbsp;grPublisher.query();<br>&nbsp;if (grPublisher.next()) {<br>&nbsp; grPublisher.setValue('manufacturer', publlisherToCoreCompany[key]);<br>&nbsp; grPublisher.update();<br><br>&nbsp; var grSoftwareModel = new GlideRecord('cmdb_software_product_model');<br>&nbsp; grSoftwareModel.addQuery('manufacturer', publlisherToCoreCompany[key]);<br>&nbsp; grSoftwareModel.query();<br>&nbsp; while(grSoftwareModel.next()) {<br>&nbsp; &nbsp;new SAMPSWModelUtil().calculateSoftwareModelName(grSoftwareModel);<br>&nbsp; &nbsp;global.ModelUtils.calculateDisplayName(grSoftwareModel);<br>&nbsp; &nbsp;grSoftwareModel.setWorkflow(false);<br>&nbsp; &nbsp;grSoftwareModel.update();<br>&nbsp; }<br>&nbsp;}<br>});</td></tr></tbody></table>
    
      
      
    
2.  Note :  
    This script is to fix issues with the above publishers mentioned in publlisherToCoreCompany.  
    Also before executing the script , verify the publisher name and core company sysid already present in the instance.  
    Create a Change for this script execution and run it as a maint user.  
    
3.  Verify Software Discovery Models contains appropriate Publisher.  
      
    ![](sys_attachment.do?sys_id=75d27085db40b4d0b55f0b55ca96190f)  
      
    
4.  Verify Correct Manufacturer for Software Publisher.  
      
    ![](sys_attachment.do?sys_id=fdd27085db40b4d0b55f0b55ca96190d)  
      
    

## Additional Information

**Useful docs:  
**

-   [Changing normalized company names](https://docs.servicenow.com/csh?topicname=c_NormalChangingNames.html&version=latest "Changing normalized company names")
-   [Supported software publisher licenses](https://docs.servicenow.com/csh?topicname=sam-publisher-packs.html&version=latest "Supported software publisher licenses")
