---
title: "Solaris server Discovery failed with IRE errors"
aliases:
  - KB0787427
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787427
kb_number: KB0787427
last_modified: 2024-04-08
---

## Solaris server Discovery failed with IRE errors

  

### Issue

Solaris Server Discovery Pattern fails with below error.

**Identification CI Errors:**  
  
**In payload missing minimum set of input values for criterion (matching) attributes from identify rule for table \[cmdb\_ci\_solaris\_instance\]**.Add these input values in payload item '{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"am-irisp-d001","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}}',Too many other errors,In payload missing minimum set of input values for criterion   
(matching) attributes from identify rule for table \[cmdb\_ci\_solaris\_instance\]. Add these input values in payload item '{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"am-iclimsp-d001","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}}  
',Too many other errors,In payload missing minimum set of input values for criterion (matching) attributes from identify rule for table \[cmdb\_ci\_solaris\_instance\].  
  

**Syslogs**  
  
**{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"eagletest","correlation\_id"**:"1ddcf9ae-7b42-c08b-a4d7-a9b2e29332e3","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}},lookup:\[\],related:\[\]  
{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"am-irisp-d001","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}},lookup:\[\],related:\[\]  
{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"am-iclimsp-d001","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}},lookup:\[\],related:\[\]  
{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"am-slimsp-d001","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}},lookup:\[\],related:\[\]  
{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"icolimpacs","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}},lookup:\[\],related:\[\]  
{"className":"cmdb\_ci\_solaris\_instance","values":{"discovery\_source":"ServiceNow","name":"pacs-dev","state":"off","sys\_class\_name":"cmdb\_ci\_solaris\_instance"}},lookup:\[\],related:\[\]

### Release

Observed post upgrading to Newyork

### Cause

The issue observed because the Solaris Server pattern was unable to populate correlation -id for Solaris instance CI's. Since the Solaris instances are identified by correlation id, the IRE engine threw the error.

**Quick verification** why the pattern was unable to populate the correlation id for Solaris instances: 

1.  The correlation id is retrieved in step 20.3. get UUID in Solaris - Zones shared the library of the Solaris Server Pattern
2.  The step executes the following command "#zoneadm list -cip"
3.  Manually execute "#zoneadm list -cip" on the Solaris host, should give output as below  
      
    
    <table style="height: 66px; width: 30.5447%; border-collapse: collapse;"><tbody><tr><td style="width: 100%; background-color: #f2f0f0;">0:<span style="color: #ff0000;"><strong>global</strong></span>:running:/::native:shared<br>1:xxxx:running:/<span style="color: #ff0000;"><strong>global</strong></span>/zones/xxxx:xxxx-xxxx-xx-ab94-d39101a89ca0:solaris8:shared<br>2:xxxx:running:/<strong><span style="color: #ff0000;">global</span></strong>/zones/xxxx-xxxx:xxxx-xx-65d9-9xc8664b309fcc:native:shared</td></tr></tbody></table>
    
      
      
    
4.  The Step configured as it should include the string "global" 
5.  Looking at the above output, each line contains the string "global", the whole data is excluded and therefore we are not able to parse the UUID (Correlation id ) from the result.

### Resolution

1.  Log in to the instance 
2.  Navigator >> Pattern Designer >> Discovery Patterns   
      
    
    <table style="height: 13px; width: 26.5713%; border-collapse: collapse;"><tbody><tr style="height: 13px;"><td style="width: 100%; height: 13px; background-color: #f2f0f0;">https://&lt;Instancename&gt;.service-now.com/sn_discovery_patterns_list.do</td></tr></tbody></table>
    
      
      
    
3.  In the Name field, search for the pattern "Solaris Server" and open the record   
      
    
    https://<Instancename>.service-now.com/$sn\_pattern\_designer.do?authoring\_mode=modify&sys\_id=1826ee364f47e200c7e881c18110c7aa&sysparm\_view=&sysparm\_record\_target=sa\_pattern&sysparm\_record\_row=1&sysparm\_record\_list=nameCONTAINSSolaris+Se%5EORDERBYname&sysparm\_record\_rows=1In the Identification section >> Click on "Discovery" to go into Debug mode.
    
4.  Left side >> Go to Step No 20.3 "get uuid"
5.  In the "Exclude Lines" section modify the default value from "global" to ":global:"   
      
            ![](/sys_attachment.do?sys_id=f1ae9085db0c70905a959c41ba96195a)  
      
    
6.  Save the Pattern 
7.  Publish the Pattern  
8.  Execute a Quick Discovery
