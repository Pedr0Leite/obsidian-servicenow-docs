---
title: "Post-Processing Manager for Users in non-LDAP User Import"
aliases:
  - KB0533666
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0533666
kb_number: KB0533666
last_modified: 2024-04-07
---

## Post-Processing Manager for Users in non-LDAP User Import

  

### Issue

 For LDAP integrations, ServiceNow provides the _LDAPUtil_ script include and its process manager function to populate managers that may be missing when a user is inserted or updated. There does not appear to be a stock equivalent for users who are loaded from a non-LDAP source, such as a flat file or database. The _LDAPUtil_ script include further leverages Java classes that cannot be modified or modeled to support a similar process on non-LDAP loads.  Since these types of user loads could also insert or update a user that references a manager who does not yet exist, there is a need for a similar solution.

  

### Resolution

**Option 1:** Create a second transform map that is ordered higher that transforms the same import set after the initial load to update the manager field. This is a very simple solution, but causes the entire import set to be reprocessed when the condition probably only exists on a small handful of records. Depending on the population of users in your system, this may or may not be acceptable.

**Option 2:** Map the manager and set the map to create the missing record. If the key that is used to identify the manager is the same key field used to coalesce the user transform map, the manager record will be created with minimal information (just the key) and the subsequent update will populate the remaining information when the manager record is ultimately found. This avoids multiple passes and post processing, but could potentially result in skeletal records because there is a possibility that the referenced manager will never be loaded. This should not be the case, but it is possible. It does require that you coalesce on the same value that you are using to identify the manager. This is probably usually the case, but there has been at least one case where it was not.

**Option 3:** This option involves a script include and several transform map scripts but has the advantage of only firing on the records that need to be updated. If you have 100k records, you won't have to process 100k records twice the same way you would in the first solution. It doesn't require that customers use the same key for the manager as they do for the map coalesce or that they create skeletal user records for users that were never created.

1.  Map the manager field using whatever key is appropriate and set the choice action to **create**. While this sounds counterintuitive, it will later allow you to leverage an onForeignInsert script to identify failed mappings.![](/sys_attachment.do?sys_id=8c7ae466db42b450e515c22305961979)
2.  Create an onStart transform map script for the sole purpose of declaring and initializing an array with adequate scope:  
      
    //Setup array of records to have managers reprocessed.  
    var reprocessManagers = \[\];
3.  Create an onForeignInsert script that checks to see if the insert is for the manager field and pushes the value into our array. Setting **ignore equal to true** in this context causes the reference insert to be skipped, which is what you always want to do. Our user import should ultimately bring this record in its entirety into the system. However, you will have managed to capture the failed insert in the array. 
    
    //Collect missing managers for post-processing  
    if (name == 'manager') {
    
    > reprocessManagers.push(source.sys\_id + '');
    
    > ignore=true;
    
    }
4.  Create a script include that can be called from the transform map upon completion in order to process the array of source records that were not available during the initial transform. **Note**: This script include is very specific to the customer for which it was implemented. It can be modified or generalized to suit  other customers, but it is listed here to demonstrate the approach.
    
    var UserImportUtil = Class.create();  
    UserImportUtil.prototype = {
    
    > initialize: function() {
    
    > },
    
      
    processManagers: function(reprocessArray, table) {  
    
    > //Get all rows that resolved to a target  
    > var importRows = new GlideRecord(table);  
    > importRows.addQuery('sys\_id','IN',reprocessArray);  
    > importRows.addNotNullQuery('sys\_target\_sys\_id');
    > 
    > importRows.query();
    > 
    > while (importRows.next()) {
    > 
    > > if (!JSUtil.nil(importRows.u\_manager\_employee\_nbr)) {
    > 
    > > > //Get the manager
    > 
    > > > var managerGR = new GlideRecord('sys\_user');
    > 
    > > > if (managerGR.get('email',importRows.u\_manager\_employee\_nbr)) {  
    > > > 
    > > > > //Get record to update  
    > > > > var targetGR = new GlideRecord(importRows.sys\_target\_table);  
    > > > > if (!JSUtil.nil(importRows.sys\_target\_sys\_id) && targetGR.get(importRows.sys\_target\_sys\_id)) {  
    > > > 
    > > > > > targetGR.manager = managerGR.sys\_id;  
    > > > > > targetGR.update();
    > > 
    > > > > }
    > > > 
    > > > }
    > 
    > > }
    > 
    > }
    
    },  
      
    type: 'UserImportUtil'  
    };
5.  Finally, add an onComplete script to the transform map to call the script include and process the array of values that were accumulated in the onForeignInsertscript:
    
    //Handles the cases where the manager is not present when updating  
    var userImportUtil = new UserImportUtil();
    
    userImportUtil.processManagers(reprocessManagers, 'u\_import\_users');
    

**Conclusion:** This approach will now only perform database operations and loop through the records for which this condition exists, significantly reducing the overhead of post-processing.
