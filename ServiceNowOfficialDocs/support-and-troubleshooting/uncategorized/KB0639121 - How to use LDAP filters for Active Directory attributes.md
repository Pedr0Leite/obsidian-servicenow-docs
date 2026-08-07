---
title: "How to use LDAP filters for Active Directory attributes"
aliases:
  - KB0639121
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639121
kb_number: KB0639121
last_modified: 2026-05-04
---

## How to use LDAP filters for Active Directory attributes

  

### Issue

Using LDAP filters is very helpful when fetching the relevant data into your SN instance from the Active Directory. It is always advisable to test the filters within the instance while browsing your AD to avoid errors. Below is the sequence of recommended steps:

1.  Open the **LDAP Server** in question listed in the configuration table: _https://<instance>.service-now.com/ldap\_server\_config\_list.do_
2.  Open the required **Organization Unit** from the OU table: _https://<instance>.service-now.com/ldap\_ou\_config\_list.do_
3.  Click **Browse**
4.  In the **Filter** box, start with a basic filter like **objectClass=person**, to display all AD identified actual users
5.  Click the **Filter** button
6.  Select a **User** from the list
7.  Observe on the right the **Attribute Name** and the corresponding **Attribute Value**   
      
    ![](sys_attachment.do?sys_id=34365a614797aa102c31b98a436d4377)  
    -   If you do not find an attribute in the list, make sure it is present and populated in the AD, because attributes with no assigned value are not visible.
    -   It is essential to have at least one record populated for each attribute in the AD, for it to be available in the transform map, and to map the AD and the instance fields.
8.  Depending on the AD value required, **adjust the filter** by following the standard LDAP filter syntax and test whether the filter applied returns the expected result. 

![](sys_attachment.do?sys_id=f0365a614797aa102c31b98a436d437a)

### Release

All releases

### Resolution

For your library, the most commonly used LDAP filters can be found on these websites:

-   [http://www.ldapexplorer.com/en/manual/109050000-famous-filters.htm](http://www.ldapexplorer.com/en/manual/109050000-famous-filters.htm)
-   [https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx#Examples](https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx#Examples)
