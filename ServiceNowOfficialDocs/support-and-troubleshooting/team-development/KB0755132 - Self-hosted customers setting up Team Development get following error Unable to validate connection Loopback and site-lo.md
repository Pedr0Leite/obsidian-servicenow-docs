---
title: "Self-hosted customers setting up Team Development get following error: \"Unable to validate connection: Loopback and site-local URLs are not supported. Provide the URL of another instance\"
aliases:
  - KB0755132
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755132
kb_number: KB0755132
last_modified: 2025-12-29
---

## Self-hosted customers setting up Team Development get following error: "Unable to validate connection: Loopback and site-local URLs are not supported. Provide the URL of another instance"

  

### Issue

Self-hosted customers setting up Team Development may get the following error: "**Unable to validate connection: Loopback and site-local URLs are not supported. Provide the URL of another instance**".

### Steps to reproduce

1.  Navigate to **Team Development > Remote Instances**.
2.  Click **New**.
3.  Enter the information for the user login credentials and hostname for a remote instance.
4.  Click **Test Connection**
5.  The error message is displayed

### Release

Please refer to the Resolution section.

### Cause

The "**glide.update\_set.remote.check\_host**" property is defaulted to "**true**" in the instances.

### Resolution

Log in to the instances and check for name "glide.update\_set.remote.check\_host" in system properties. If you do not find it, try to create the system property record from UI with following values: 

Name : **glide.update\_set.remote.check\_host**   
type : **True/False**   
value : **false** 

Should this fail, you will need to update or create this property in the database, with the following SQL: 

SELECT \* FROM sys\_properties WHERE name='glide.update\_set.remote.check\_host';

If the property exists but has the 'value' column set to "true", run the following:

UPDATE sys\_properties set value='false' WHERE name='glide.update\_set.remote.check\_host';

If the property doesn't exist (as is the case in my instance), create it in the database like so: 

-   first generate from instance Background scripts a new sys\_id:

              **gs.print(new GlideGuid.generate(null));**

-   copy the sys\_id into the INSERT statement (make sure you replace the sys\_id in red with the value you got generated):

         INSERT INTO sys\_properties (name, suffix, type, description, choices, is\_private, ignore\_cache, value, sys\_id, read\_roles, write\_roles) VALUES ('glide.update\_set.remote.check\_host', 'glide.update\_set.remote.check\_host', 'boolean', NULL, NULL, 0, 0, 'false', '**df34bce3db4fc4d0cdec8324399619fd**', NULL, NULL);  
         INSERT INTO sys\_metadata (sys\_class\_name, sys\_name, sys\_update\_name, sys\_id, sys\_updated\_by, sys\_updated\_on, sys\_created\_by, sys\_created\_on, sys\_mod\_count, sys\_scope, sys\_package, sys\_policy) VALUES ('sys\_properties', 'glide.update\_set.remote.check\_host', 'sys\_properties\_**df34bce3db4fc4d0cdec8324399619fd**', '**df34bce3db4fc4d0cdec8324399619fd**', 'sergiu.panaite@snc', '2020-02-12 13:17:20', 'sergiu.panaite@snc', '2020-02-12 13:17:20', 0, 'global', 'global', NULL);

After doing either of the above, log back into the instance, and clear the cache of the properties by running the following script in "Scripts - Background":

GlidePropertiesDB.invalidate();

Finally, restart the instances.

**Note**: The above SQL commands are meant for MariaDB installations only! Should your company's instances be running on Oracle, you will need to convert the SQL.
