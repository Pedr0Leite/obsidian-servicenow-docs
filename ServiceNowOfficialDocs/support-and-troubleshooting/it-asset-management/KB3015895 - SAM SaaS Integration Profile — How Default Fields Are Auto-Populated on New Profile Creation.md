---
title: "SAM SaaS Integration Profile — How Default Fields Are Auto-Populated on New Profile Creation"
aliases:
  - KB3015895
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3015895
kb_number: KB3015895
last_modified: 2026-05-12
---

## SAM SaaS Integration Profile — How Default Fields Are Auto-Populated on New Profile Creation

  

### Summary

When creating a new SAM SaaS integration profile on the samp\_sw\_subscription\_profile table, certain fields such as Download Consumption Subflow, Download Subscription Subflow, Reclaim Subscription Subflow, Activity Subscription Subflow, and Connection Credential are automatically populated by the platform before the record is saved.

This article explains the OOB mechanism behind this behavior and provides troubleshooting steps when the fields do not populate as expected.

─────────────────────────────────  
**HOW IT WORKS**

The auto-population is driven by four components working in sequence every time the samp\_sw\_subscription\_profile form loads for a new record.

Step 1 — Display Business Rule: Set profile form config on scratchpad  
This before\_display business rule fires on form load and calls SAMSaasIntegrationUtils.getProfileFormConfig(), passing the profile\_type of the current record. The result is stored in g\_scratchpad.profile\_form\_config for client scripts to consume.

Step 2 — sam\_saas\_script\_route lookup  
Inside getProfileFormConfig, a call is made to getIntegrationObject(profileType), which queries the sam\_saas\_script\_route table for a row matching the current profile\_type. This table maps each profile\_type to a specific script include and scope. The matched script include is instantiated and its getProfileFormConfig() method is called.

Note: sam\_saas\_script\_route is scoped to sn\_sam\_saas and is not readable via the REST API due to cross-scope access restrictions. It can be queried server-side via a background script using GlideRecord.

Step 3 — sam\_saas\_profile\_type\_default\_value lookup  
The instantiated script include queries the sam\_saas\_profile\_type\_default\_value table for all rows where profile\_type matches the current profile. Each row defines one field and its default value. The result is returned as an object with isValid set to true and a defaultValues array containing the field and value pairs, stored in g\_scratchpad.profile\_form\_config.

Step 4 — OnLoad Client Script: SAMSaas configure profile config default  
This client script reads g\_scratchpad.profile\_form\_config. When isValid is true and the record is new, it loops through the defaultValues array and calls g\_form.setValue() for each entry, setting the default fields on the form before the user saves the record.

─────────────────────────────────  
**TROUBLESHOOTING**

If default fields are not auto-populating when creating a new profile, work through the following checks in order.

Check 1 — Verify the sam\_saas\_script\_route entry exists for the profile type

Run the following background script on the affected instance, replacing the profileType value with the affected profile type:

   var profileType = 'crowdstrike\_subscription';  
   var gr = new GlideRecord('sam\_saas\_script\_route');  
   gr.addQuery('profile\_type', profileType);  
   gr.query();  
   while (gr.next()) {  
     gs.log('scope: ' + gr.getValue('scope'), 'SAM\_DEBUG');  
     gs.log('script\_include: ' + gr.getValue('script\_include'), 'SAM\_DEBUG');  
   }  
   if (gr.getRowCount() == 0) {  
     gs.log('NO entry found for ' + profileType, 'SAM\_DEBUG');  
   }

If no entry is found, the getIntegrationObject call will throw an error and getProfileFormConfig will return isValid as false. No default fields will be set. Compare with a reference instance on the same version and patch level and insert the missing row.

Check 2 — Verify the sam\_saas\_profile\_type\_default\_value rows exist for the profile type

   var profileType = 'crowdstrike\_subscription';  
   var gr = new GlideRecord('sam\_saas\_profile\_type\_default\_value');  
   gr.addQuery('profile\_type', profileType);  
   gr.query();  
   while (gr.next()) {  
     gs.log('field: ' + gr.getValue('field') + ' | value: ' + gr.getValue('value'), 'SAM\_DEBUG');  
   }  
   if (gr.getRowCount() == 0) {  
     gs.log('NO default value rows found for ' + profileType, 'SAM\_DEBUG');  
   }

If no rows are found, the defaultValues array returned to the client script will be empty and no fields will be set. Insert the missing rows by comparing with a reference instance on the same version and patch level.

Check 3 — Verify the display BR and client script are active

Confirm the following are active on samp\_sw\_subscription\_profile:  
\- Business Rule (before\_display): Set profile form config on scratchpad  
\- Client Script (onLoad): SAMSaas configure profile config default

If either is inactive, g\_scratchpad.profile\_form\_config will either not be set or not be consumed, and the fields will not populate.

Check 4 — Verify the mapped script include implements getProfileFormConfig

If Check 1 returns a valid entry but fields are still not populating, confirm the script include identified in sam\_saas\_script\_route implements a getProfileFormConfig method. If the method does not exist, getProfileFormConfig in SAMSaasIntegrationUtils falls back to a default config object that contains no defaultValues, and no fields will be set.

─────────────────────────────────  
**KEY TABLES**

\- sam\_saas\_script\_route — Maps each profile\_type to its integration script include and scope  
\- sam\_saas\_profile\_type\_default\_value — Stores the default field values per profile\_type  
\- samp\_sw\_subscription\_profile — The integration profile record
