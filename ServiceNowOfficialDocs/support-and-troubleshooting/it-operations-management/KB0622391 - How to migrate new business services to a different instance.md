---
title: "How to migrate new business services to a different instance"
aliases:
  - KB0622391
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622391
kb_number: KB0622391
last_modified: 2025-01-03
---

## How to migrate new business services to a different instance

  

### Issue

 **Warning:** The purpose of this article is to assist with migrating NEW business services (with entry points that were not used as entry points of any existing business services) from one Service Now instance to the other. Do not use the scripts supplied with this article to migrate modified (existing) business services (and entry points), as it might overwrite existing data or cause duplications.  
 **\*\*\* USE WITH CAUTION \*\***

The “Add all business services to update set” script is a fix script whose purpose is to add all business services and their associated entry points to the **current** update set to make it easier for the Migration Engineer to migrate this content, initially migrated from ServiceWatch, from one ServiceNow instance to the other.

Note that the script is not limited to the migrated business services. It adds ALL business services and their entry points to the update set regardless of whether they are added with migration.

This script was implemented as a fix script because fix scripts are easy to run on demand, and doing so doesn’t require maint permissions.

For more information regarding update sets, see the documentation topic [Update sets](https://docs.servicenow.com/bundle/istanbul-application-development/page/build/system-update-sets/concept/c_UpdateSets.html) and its subtopics.

For more information regarding fix scripts, see the documentation topic [Fix\_scripts](https://docs.servicenow.com/bundle/istanbul-application-development/page/build/applications/concept/c_FixScripts.html).

### Scripts

This document provides the content for the following two fix scripts and then describes them:

-   [sys\_script\_fix\_b801dd21c3002200ab8f9624a1d3ae31.xml](#first) – "Add all business services to update set” fix script
-   [sys\_script\_fix\_90545218db852200e2c27a6eaf9619b0.xml](#second) ‐ "Synchronize BS with Service Model” fix script

### sys\_script\_fix\_b801dd21c3002200ab8f9624a1d3ae31.xml ‐ “Add all business services to update set” fix script

<?xml version="1.0" encoding="UTF-8"?>   
<unload unload\_date="2016-08-01 08:27:26">  
<sys\_script\_fix action="INSERT\_OR\_UPDATE">  
<active>true</active>  
<before>false</before>  
<description/>  
<flush\_cache>false</flush\_cache>  
<name>Add all business services to update set</name>  
<run\_once>true</run\_once>  
<script><!\[CDATA\[var setID = gs.getPreference('sys\_update\_set'); var us = new GlideRecord('sys\_update\_set');  
if (us.get(setID)) { gs.log("About to add all business service groups to update set id=" + setID + " (" + us.name + ")"); addBsGroupsToUpdateSet();  
gs.log("About to add all business services and their entry points to update set id=" + setID + " (" + us.name + ")"); addToUpdateSet(); }  
function addBsGroupsToUpdateSet()  
{ var um = new GlideUpdateManager2();  
var gr = new GlideRecord('cmdb\_ci\_service\_group'); gr.query();  
while (gr.next()) { um.saveRecord(gr);  
gs.log('Business Service Group id=' + gr.sys\_id + ' (' + gr.name + ') added to update set'); } }  
function addToUpdateSet() {  
var um = new GlideUpdateManager2();  
var m2mGr = new GlideRecord('sa\_m2m\_service\_entry\_point'); m2mGr.query();  
while (m2mGr.next()) {  
var m2mId = m2mGr.getValue('sys\_id');  
var bsId = m2mGr.getValue('cmdb\_ci\_service');  
var epId = m2mGr.getValue('cmdb\_ci\_endpoint');
var bsGr = new GlideRecord  
('cmdb\_ci\_service\_discovered');  
if (bsGr.get(bsId)) {  
bsGr.setValue('layer','');  
um.saveRecord(bsGr);  
gs.log('Business Service id=' + bsId + ' (' + bsGr.name + ') added to update set'); }
var groupGr = new GlideRecord('sa\_service\_group\_member');  
groupGr.addQuery('service', bsId);  
groupGr.query();  
while (groupGr.next())   
{ um.saveRecord(groupGr);  
gs.log('Association of Business Service id=' + bsId + ' to group id=' + groupGr.service\_group + ' added to update set'); }
var epGr = new GlideRecord('cmdb\_ci\_endpoint');  
if (epGr.get(epId)) {  
// Getting the specific ep  
var clazz = epGr.getValue('sys\_class\_name');  
var specificEpGr = new GlideRecord(clazz);  
if (specificEpGr.get(epId))   
{ um.saveRecord(specificEpGr);  
gs.log('Entry Point id=' + epId + ' (' + specificEpGr.name + ') of type ' + clazz + ' added to update set');   
         }   
}  
var assocGr = new GlideRecord('svc\_ci\_assoc');  
assocGr.addQuery('service\_id',bsId);  
assocGr.addQuery('ci\_id',epId);  
assocGr.query();  
if (assocGr.next()) {  
um.saveRecord(assocGr); gs.log('Association of endpoint id=' + epId + ' to service id=' + bsId + ' added to update set'); }
um.saveRecord(m2mGr);  
gs.log('M2m record id=' + m2mId + 'added to update set');  
} }\]\]></script>  
<sys\_class\_name>sys\_script\_fix</sys\_class\_name>  
<sys\_created\_by>admin</sys\_created\_by>  
<sys\_created\_on>2016-06-16 07:37:26</sys\_created\_on>  
<sys\_customer\_update>false</sys\_customer\_update>  
<sys\_id>b801dd21c3002200ab8f9624a1d3ae31</sys\_id>  
<sys\_mod\_count>5</sys\_mod\_count>  
<sys\_name>Add all business services to update set</sys\_name>  
<sys\_package display\_value="Global">global</sys\_package>  
<sys\_policy/>  
<sys\_replace\_on\_upgrade>false</sys\_replace\_on\_upgrade>  
<sys\_scope display\_value="Global">global</sys\_scope>  
<sys\_update\_name>sys\_script\_fix\_b801dd21c3002200ab8f9624a1d3ae31</sys\_update\_name>  
<sys\_updated\_by>admin</sys\_updated\_by>  
<sys\_updated\_on>2016-08-01 08:05:31</sys\_updated\_on>  
<unloadable>true</unloadable>  
</sys\_script\_fix>  
</unload>

### sys\_script\_fix\_90545218db852200e2c27a6eaf9619b0.xml - “Synchronize BS with Service Model” fix script

<?xml version="1.0" encoding="UTF-8"?>  
<unload unload\_date="2016-08-01 08:34:01">  
<sys\_script\_fix action="INSERT\_OR\_UPDATE">  
<active>true</active>  
<before>false</before>  
<description/>  
<flush\_cache>false</flush\_cache>  
<name>Synchronize BS with Service Model</name>  
<run\_once>true</run\_once>  
<script><!\[CDATA\[if (GlideProperties.getBoolean  
('sa.service\_modeling.use', true)) {  
var utils = new ServiceMappingUtils();  
var gr = new GlideRecord('cmdb\_ci\_service\_discovered');  
gr.query();  
while (gr.next()) {  
   if (gr.layer == '') {  
      utils.resetModel(gr);  
      }  
   }  
}  
   else {  
      gs.log("\*\*\* sa.service\_modeling.use property is false \*\*\*");  
      }  
\]\]></script>  
<sys\_class\_name>sys\_script\_fix</sys\_class\_name>  
<sys\_created\_by>tal.benari</sys\_created\_by>  
<sys\_created\_on>2016-08-01 08:21:22</sys\_created\_on><sys\_customer\_update>false</sys\_customer\_update>  
<sys\_id>90545218db852200e2c27a6eaf9619b0</sys\_id>  
<sys\_mod\_count>4</sys\_mod\_count>  
<sys\_name>Synchronize BS with Service Model</sys\_name>  
<sys\_package display\_value="Global">global</sys\_package>  
<sys\_policy/>  
<sys\_replace\_on\_upgrade>false</sys\_replace\_on\_upgrade>  
<sys\_scope display\_value="Global">global</sys\_scope>  
<sys\_update\_name>sys\_script\_fix\_90545218db852200e2c27a6eaf9619b0</sys\_update\_name>  
<sys\_updated\_by>admin</sys\_updated\_by>  
<sys\_updated\_on>2016-08-01 08:33:52</sys\_updated\_on>  
<unloadable>true</unloadable>  
</sys\_script\_fix> </unload>

  

### Script Logic

-   The script starts by adding all existing Business Service Groups to the update set.
-   It then queries the sa\_m2m\_service\_entry\_point table, which binds business services to endpoint records, making them the business service’s entry points.
-   It uses each record to fetch the business service (cmdb\_ci\_service\_discovered) record and the endpoint (cmdb\_ci\_endpoint) record, using their sys\_ids.
-   To find out the exact endpoint type, it uses the sys\_class\_name field in the cmdb\_ci\_endpoint record. The specific endpoint record is fetched using this field’s contents.
-   To find out which group each service is bound to, it uses the business service’s sys\_id to fetch the group member records (sa\_service\_group\_member).
-   Using the sys\_ids of the business service and endpoint records, it also fetches the CI association (svc\_ci\_assoc) record. (This is most important in Geneva, where the current map nodes are based on CI associations.)
-   Finally, the m2m record, group member record, CI association record, business service record and specific endpoint record are all added to the update set. The script uses the GlideUpdateManager2 API to do that.
-   Messages printed to the log let the user know which records were added to the update set.

### How to use the script

1.  Make sure that the update set you want to add the business services to is your current update set. If not, make it current.
    
    For more information, see the documentation topic [Update sets](https://docs.servicenow.com/bundle/istanbul-application-development/page/build/system-update-sets/concept/c_UpdateSets.html).
    
2.  Import the “Add all business services to update set” fix script XML to the instance.
    
      
    1.  Navigate to **System Definition** > **Upload File**.
    2.  Browse to choose the file.
    3.  Click the **Upload** button.
3.  Navigate to **System Definition** > **Fix Scripts** and search for the fix script.
    
4.  On the fix script form, click the **Run Fix Script** related link, and click **OK**.
    
5.  Click either **Proceed** or **Proceed in Background**.
    
      
    -   **Proceed** – Runs the script interactively. When the script finishes, a window displays a script log that shows which records were added to the update set. You can copy this log and save it elsewhere for future reference.
    -   **Proceed in Background** – Click the **Show Program Workers** link in the fix script form to go to the Progress Workers table to monitor the script’s progress. The script log will appear in the Message field of the relevant Progress Worker.
6.  When you are done, click **Close** and go to your update set to see that the records were added.
    

### Important Notes

-   After importing the update set to the target instance, you need to synchronize all business services with Service Model through the related UI action. The script removes the reference to the layer prior to adding the business service record to the update set without saving the business service record itself.
    
    The layer reference is removed because Service Model records are not added to the update set. Adding Service Model records to the update set and transferring them from one instance to another is unsafe as it might break the model. If the reference were to be left intact, an error message regarding a nonexistent reference to the layer would appear during import.
    
-   If you don’t have access to this UI action, upload the “Synchronize BS with Service Model” fix script to the target instance and run it the same way you ran the previous fix script on the source instance.
    
    This fix script is safe as it synchronizes only business services missing from Service Model. (Otherwise, the history of existing business services would have been reset.)
    
-   A record may appear more than once in the log. However, a record cannot exist in an update set more than once; therefore, it won’t appear as a duplicate.
    
-   When using the GlideUpdateManager2 API, a record is created in the sys\_update\_version table, and an XML file is created under the customer update folder because it is a part of the mechanism that allows adding records to an update set. It should not have any side effects because these tables are not defined as update\_synch.
