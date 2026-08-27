---
title: "How to import photos from Active Directory (AD) into ServiceNow using an LDAP Import"
aliases:
  - KB0597756
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597756
kb_number: KB0597756
last_modified: 2024-02-26
---

## How to import photos from Active Directory (AD) into ServiceNow using an LDAP Import

  

### Issue

This article explains how to import a thumbnail photo from your Active Directory server into ServiceNow using an LDAP import.

### Procedure

**Step 1: Import Set Table (u\_thumbnail)**

If you use the import set table (ldap\_import) to import users, ensure that there is a u\_thumbnail (or similar) column with string(13,500). This column is usually created by your LDAP user import. 

1.  Use the following URL: /sys\_dictionary\_list.do?sysparm\_query=name%3Dldap\_import%5Eelement%3Du\_thumbnailphoto  
      
    13,500 is an estimated value; you may need a larger size for your thumbnails.

**Step 2: LDAP and MID Server Binary Attributes**

Add the value **thumbnailphoto** to the system property glide.ldap.binary\_attributes.

1.  Use the following URL: /sys\_properties\_list.do?sysparm\_query=name%3Dglide.ldap.binary\_attributes   
      
    The value for the system property should be similar to: objectsid, thumbnailphoto.  
     
2.  In MID Server Properties, use the following URL: /ecc\_agent\_property\_list.do?sysparm\_query=name%3Dglide.ldap.binary\_attributes[  
      
    ](https://\<yourinstance\>.service-now.com/ecc_agent_property_list.do?sysparm_query=name%3Dglide.ldap.binary_attributes)
3.  Add the value **thumbnailphoto** to the system property glide.ldap.binary\_attributes.  
      
    Restart MID SERVER - MID Properties are read during start-up. 

**Step 3: Add Transform Script**

Add a transform script to your LDAP user import transform map.

 **Note:** This is a sample OnAfter script and is not supported by ServiceNow to import thumbnail photos.

**Transform Map Script:** OnAfter

**Script**:

```
//gs.log('User Photo Script: Check for Existing Attachment');
var grPhotoAttachmentExists = new GlideRecord('sys_attachment');
grPhotoAttachmentExists.addQuery('table_name', 'ZZ_YYsys_user');
grPhotoAttachmentExists.addQuery('table_sys_id', target.sys_id);
grPhotoAttachmentExists.addQuery('file_name', 'photo');
grPhotoAttachmentExists.query();
if (source.u_thumbnailphoto != '') {
    //gs.log('User Photo Script: LDAP Source Photo Exists'); 
    if (!grPhotoAttachmentExists.next()) {
        //gs.log('User Photo Script: No existing photo attachment, attach new photo'); 
        attachPhoto();
    } else {
        //gs.log('User Photo Script: Photo Attachment Exists, Compare Attachments'); 
        var sysEncodedAttachment = new GlideSysAttachment();
        var binData = sysEncodedAttachment.getBytes(grPhotoAttachmentExists);
        var EncodedBytes = GlideStringUtil.base64Encode(binData);
        if (EncodedBytes != source.u_thumbnailphoto) {
            //gs.log('User Photo Script: Photo attachment exists, bytes don't match, delete existing attachment and attach new photo'); 
            grPhotoAttachmentExists.deleteRecord();
            attachPhoto();
        }
    }
} else {
    //gs.log('User Photo Script: LDAP Source Photo Does Not Exist'); 
    if (grPhotoAttachmentExists.next()) {
        //gs.log('User Photo Script: Delete existing photo attachment'); 
        grPhotoAttachmentExists.deleteRecord();
    }
}

function attachPhoto() {
    //gs.log('User Photo Script: Attach Photo'); 
    var sysDecodedAttachment = new GlideSysAttachment();
    var DecodedBytes = GlideStringUtil.base64DecodeAsBytes(source.u_thumbnailphoto);
    var attID = sysDecodedAttachment.write(target, 'photo', 'image/jpeg'
        , DecodedBytes);
    var newAttachment = new GlideRecord("sys_attachment");
    newAttachment.addQuery("sys_id", attID);
    newAttachment.query();
    if (newAttachment.next()) {
        newAttachment.table_name = "ZZ_YYsys_user";
        newAttachment.table_sys_id = target.sys_id;
        newAttachment.content_type = 'image/jpeg';
        newAttachment.update();
    }
}
```

**Step 4: Limit Import**

Limit your LDAP user import to only a few users so you can test. It is safer and quicker to test one user rather than 10,000.

1.  In your [LDAP OU Definition for LDAP Users](https://docs.servicenow.com/csh?topicname=t_DefineLDAPOrganizationalUnits.html&version=latest "LDAP OU Definition"), add a filter.    
    For example: (sAMAccountName=joe.employee)
2.  On the LDAP OU Definition for LDAP Users, click **Browse**.
3.  To verify that only one user is returned, click the plus sign on the LDAP Nodes.

**Step 5:  Add the Photo Field**

1.  On the user form, right-click in the header bar and select **Configure > Form Layout**.
2.  Add the **Photo** field to the form.
3.  Click **Save**.

**Step 6: Test**

1.  Navigate to **System Import Sets > Administration > Scheduled Imports**.
2.  Open LDAP User Import.
3.  Click **Execute Now**.
4.  Wait until import finishes.    
    You can check [active transactions](https://docs.servicenow.com/csh?topicname=t_ViewAndKillAnActiveTransaction.html&version=latest "active transactions") to see if the process is running.
5.  Check **Imported User**.
6.  Remember to change LDAP OU Definition back to import all users.
7.  Run the scheduled import for all users again.

**Step 7: Troubleshooting**

-   Check the system property "**glide.attachment.extensions**" and remove the data in the value field. The list of file extensions (comma-separated) can be attached to documents via the attachment dialog. Extensions should not include the dot (.) e.g. xls, xlsx, doc, docx. Leave blank to allow all extensions. 
-   You may need to increase the u\_thumbnail column to a size larger than 13500 (for example, if some pictures are not imported)
-   Watch the warning and error logs during import
-   The transform script includes some gs.log statements you can uncomment out for debugging

Some forum posts mention setting the system property com.glide.loader.verify\_target\_field\_size to true. This property controls if import set fields can automatically increase in size during an import (true) or not (false). By default, data that exceeds the import field size is truncated. Set this property to true to allow any import set field to increase the column size to match the length of the data. This is not the best practice. Instead, manually set the size of the u\_thumbnail column as in Step 1 (Import Set Table (u\_thumbnail)) above.  Some columns in LDAP that store credentials are very large. If you use this property, you may receive this error and not be able to import any LDAP records:

java.sql.SQLException: java.sql.BatchUpdateException: Row size too large. The maximum row size for the used table type, not counting BLOBs, is 8126. You have to change some columns to TEXT or BLOBs

If you use the com.glide.loader.verify\_target\_field\_size property and received the error, here are steps to fix the issue:

1.  Set system property com.glide.loader.verify\_target\_field\_size to **false**.
2.  If needed, set the LDAP attributes to limit fields that are imported.
3.  Delete the columns in the ldap\_import table that are too large.  
    There may be 2 or 3 large fields.
4.  Reimport the LDAP users.  
    The columns are recreated in smaller sizes. 

### Release

### Cause

### Resolution

### Related Links

-   [http://www.servicenowelite.com/blog/2014/2/18/import-user-photo-from-ldap](http://www.servicenowelite.com/blog/2014/2/18/import-user-photo-from-ldap)
